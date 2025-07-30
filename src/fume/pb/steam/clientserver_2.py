#!/usr/bin/python3

import protobug

from ._pbmessage import EMsg, SteamProtobufMessage


@protobug.message
class CMsgClientGetDepotDecryptionKey(
    SteamProtobufMessage, msg_id=EMsg.ClientGetDepotDecryptionKey
):
    depot_id: protobug.UInt32 | None = protobug.field(1, default=None)
    app_id: protobug.UInt32 | None = protobug.field(2, default=None)


@protobug.message
class CMsgClientGetDepotDecryptionKeyResponse(
    SteamProtobufMessage, msg_id=EMsg.ClientGetDepotDecryptionKeyResponse
):
    eresult: protobug.Int32 | None = protobug.field(1, default=2)
    depot_id: protobug.UInt32 | None = protobug.field(2, default=None)
    depot_encryption_key: protobug.Bytes | None = protobug.field(3, default=None)
