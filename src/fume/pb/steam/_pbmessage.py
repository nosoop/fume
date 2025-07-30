#!/usr/bin/python3

import dataclasses
import typing
from typing import Self, Type

import protobug

# export the EMsg enum to simplify imports from dependent modules
from ...enum.emsg import EMsg as EMsg

_PROTOBUF_MASK = 0x80000000


class SteamMessage:
    """
    Base class for registering Steam messages.
    """

    msg_id: EMsg | None
    """ The class-specific message ID. """

    messages: dict[EMsg | None, Type[Self]] = {}
    """ A registry of EMsg values to SteamProtobufMessage types. """

    def __init_subclass__(cls, msg_id: EMsg | None, **kwargs):
        if msg_id:
            cls.messages[msg_id] = cls
            cls.msg_id = msg_id

    @classmethod
    def is_implemented_id(cls, msg_id: EMsg) -> bool:
        return msg_id in cls.messages

    @classmethod
    def loads(cls, msg_id: EMsg, body: bytes) -> Self:
        if not cls.is_implemented_id(msg_id):
            return typing.cast(Self, CMsgUnknown.loads(msg_id, body))
        return cls.messages[msg_id].loads(msg_id, body)


class SteamProtobufMessage(SteamMessage, msg_id=None):
    """
    Mixin class for registering Steam protobuf messages.
    Protobuf classes must subclass this and specify the associated EMsg value.
    """

    def __init_subclass__(cls, msg_id: EMsg | None, **kwargs):
        super().__init_subclass__(
            typing.cast(EMsg, msg_id | _PROTOBUF_MASK) if msg_id else None, **kwargs
        )
        cls.msg_id = msg_id

    @classmethod
    def loads(cls, msg_id: EMsg, body: bytes) -> Self:
        """
        Deserializes bytes as a protobuf message of the class.
        This may be overwritten if a message can be treated as a variant (e.g. RPC responses
        that are covered by the same EMsg value - in that case the class should use the same
        registration pattern.
        """
        return protobug.loads(body, cls.messages[msg_id])

    def dumps(self) -> bytes:
        return protobug.dumps(self)


@dataclasses.dataclass
class CMsgUnknown(SteamMessage, msg_id=None):
    """
    Represents a Steam protobuf message that was otherwise not implemented.
    """

    message_body: bytes

    @classmethod
    def loads(cls, msg_id: EMsg, body: bytes) -> Self:
        unk_msg = cls(body)
        unk_msg.msg_id = msg_id
        return unk_msg

    def dumps(self) -> bytes:
        return self.message_body
