#!/usr/bin/python3

import protobug

from ._pbmessage import EMsg, SteamProtobufMessage

# https://github.com/solsticegamestudios/steam/blob/12ad1010891f977566f0827f0cba58f0e294fc0e/protobufs/steammessages_clientserver_login.proto


@protobug.message
class CMsgClientLogon(SteamProtobufMessage, msg_id=EMsg.ClientLogon):
    protocol_version: protobug.UInt32 | None = protobug.field(1, default=None)
    client_package_version: protobug.UInt32 | None = protobug.field(5, default=None)


@protobug.message
class CMsgClientLogonResponse(SteamProtobufMessage, msg_id=EMsg.ClientLogonResponse):
    eresult: protobug.Int32 | None = protobug.field(1, default=2)
    legacy_out_of_game_heartbeat_seconds: protobug.Int32 | None = protobug.field(
        2, default=None
    )
    heartbeat_seconds: protobug.Int32 | None = protobug.field(3, default=None)
    deprecated_public_ip: protobug.UInt32 | None = protobug.field(4, default=None)
    rtime32_server_time: protobug.Fixed32 | None = protobug.field(5, default=None)
    client_instance_id: protobug.UInt64 | None = protobug.field(27, default=None)
