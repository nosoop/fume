#!/usr/bin/python3

import protobug

from ._pbmessage import EMsg, SteamProtobufMessage


@protobug.message
class CMsgProtoBufHeader:
    steamid: protobug.Fixed64 | None = protobug.field(1, default=None)
    client_sessionid: protobug.Int32 | None = protobug.field(2, default=None)
    routing_appid: protobug.UInt32 | None = protobug.field(3, default=None)
    jobid_source: protobug.Fixed64 | None = protobug.field(10, default=0xFFFFFFFF_FFFFFFFF)
    jobid_target: protobug.Fixed64 | None = protobug.field(11, default=0xFFFFFFFF_FFFFFFFF)
    target_job_name: protobug.String | None = protobug.field(12, default=None)
    seq_num: protobug.Int32 | None = protobug.field(24, default=None)
    eresult: protobug.Int32 | None = protobug.field(13, default=2)
    error_message: protobug.String | None = protobug.field(14, default=None)
    auth_account_flags: protobug.UInt32 | None = protobug.field(16, default=None)
    transport_error: protobug.Int32 | None = protobug.field(17, default=1)
    messageid: protobug.UInt64 | None = protobug.field(18, default=0xFFFFFFFF_FFFFFFFF)


@protobug.message
class CMsgMulti(SteamProtobufMessage, msg_id=EMsg.Multi):
    size_unzipped: protobug.UInt32 | None = protobug.field(1, default=None)
    message_body: protobug.Bytes | None = protobug.field(2, default=None)
