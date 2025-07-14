#!/usr/bin/python3

import dataclasses
from typing import Self, Type

import protobug

# export the EMsg enum to simplify imports from dependent modules
from ...enum.emsg import EMsg as EMsg


class SteamProtobufMessage:
    """
    Mixin class for registering Steam protobuf messages.
    Protobuf classes must subclass this and specify the associated EMsg value.
    """

    msg_id: EMsg | None
    """ The class-specific message ID. """

    messages: dict[EMsg | None, Type[Self]] = {}
    """ A registry of EMsg values to SteamProtobufMessage types. """

    def __init_subclass__(cls, msg_id: EMsg | None, **kwargs):
        cls.messages[msg_id] = cls
        cls.msg_id = msg_id

    @classmethod
    def is_implemented_id(cls, msg_id: EMsg) -> bool:
        return msg_id in cls.messages

    @classmethod
    def loads(cls, msg_id: EMsg, body: bytes) -> Self:
        if not cls.is_implemented_id(msg_id):
            unk_msg = cls.messages[None](body)
            unk_msg.msg_id = msg_id
            return unk_msg
        return protobug.loads(body, cls.messages[msg_id])

    def dumps(self) -> bytes:
        return protobug.dumps(self)


@dataclasses.dataclass
class CMsgUnknown(SteamProtobufMessage, msg_id=None):
    """
    Represents a Steam protobuf message that was otherwise not implemented.
    """

    message_body: bytes

    def dumps(self) -> bytes:
        return self.message_body
