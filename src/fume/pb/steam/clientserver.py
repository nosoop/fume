#!/usr/bin/python3

import protobug

from ._pbmessage import EMsg, SteamProtobufMessage


@protobug.message
class CMsgClientServersAvailable(SteamProtobufMessage, msg_id=EMsg.ClientServersAvailable):
    @protobug.message
    class ServerTypesAvailable:
        server: protobug.UInt32 | None = protobug.field(1, default=None)
        changed: protobug.Bool | None = protobug.field(2, default=None)

    server_types_available: list[ServerTypesAvailable] = protobug.field(1)
    server_type_for_auth_services: protobug.UInt32 | None = protobug.field(2, default=None)
