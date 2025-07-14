#!/usr/bin/python3

import protobug

from ._pbmessage import EMsg, SteamProtobufMessage


@protobug.message
class CMsgClientPICSChangesSinceRequest(
    SteamProtobufMessage, msg_id=EMsg.ClientPICSChangesSinceRequest
):
    since_change_number: protobug.UInt32 | None = protobug.field(1, default=None)
    send_app_info_changes: protobug.Bool | None = protobug.field(2, default=None)
    send_package_info_changes: protobug.Bool | None = protobug.field(3, default=None)
    num_app_info_cached: protobug.UInt32 | None = protobug.field(4, default=None)
    num_package_info_cached: protobug.UInt32 | None = protobug.field(5, default=None)


@protobug.message
class CMsgClientPICSChangesSinceResponse(
    SteamProtobufMessage, msg_id=EMsg.ClientPICSChangesSinceResponse
):
    @protobug.message
    class PackageChange:
        packageid: protobug.UInt32 | None = protobug.field(1, default=None)
        change_number: protobug.UInt32 | None = protobug.field(2, default=None)
        needs_token: protobug.Bool | None = protobug.field(3, default=None)

    @protobug.message
    class AppChange:
        appid: protobug.UInt32 | None = protobug.field(1, default=None)
        change_number: protobug.UInt32 | None = protobug.field(2, default=None)
        needs_token: protobug.Bool | None = protobug.field(3, default=None)

    current_change_number: protobug.UInt32 | None = protobug.field(1, default=None)
    since_change_number: protobug.UInt32 | None = protobug.field(2, default=None)
    force_full_update: protobug.Bool | None = protobug.field(3, default=None)
    package_changes: list[PackageChange] = protobug.field(4, default_factory=list)
    app_changes: list[AppChange] = protobug.field(5, default_factory=list)
    force_full_app_update: protobug.Bool | None = protobug.field(6, default=None)
    force_full_package_update: protobug.Bool | None = protobug.field(7, default=None)


@protobug.message
class CMsgClientPICSProductInfoRequest(
    SteamProtobufMessage, msg_id=EMsg.ClientPICSProductInfoRequest
):
    @protobug.message
    class AppInfo:
        appid: protobug.UInt32 | None = protobug.field(1, default=None)
        access_token: protobug.UInt64 | None = protobug.field(2, default=None)
        only_public_obsolete: protobug.Bool | None = protobug.field(3, default=None)

    @protobug.message
    class PackageInfo:
        packageid: protobug.UInt32 | None = protobug.field(1, default=None)
        access_token: protobug.UInt64 | None = protobug.field(2, default=None)

    packages: list[PackageInfo] = protobug.field(1, default_factory=list)
    apps: list[AppInfo] = protobug.field(2, default_factory=list)
    meta_data_only: protobug.Bool | None = protobug.field(3, default=None)
    num_prev_failed: protobug.UInt32 | None = protobug.field(4, default=None)
    OBSOLETE_supports_package_tokens: protobug.UInt32 | None = protobug.field(5, default=None)
    sequence_number: protobug.UInt32 | None = protobug.field(6, default=None)
    single_response: protobug.Bool | None = protobug.field(7, default=None)


@protobug.message
class CMsgClientPICSProductInfoResponse(
    SteamProtobufMessage, msg_id=EMsg.ClientPICSProductInfoResponse
):
    @protobug.message
    class AppInfo:
        appid: protobug.UInt32 | None = protobug.field(1, default=None)
        change_number: protobug.UInt32 | None = protobug.field(2, default=None)
        missing_token: protobug.Bool | None = protobug.field(3, default=None)
        sha: protobug.Bytes | None = protobug.field(4, default=None)
        buffer: protobug.Bytes | None = protobug.field(5, default=None)
        only_public: protobug.Bool | None = protobug.field(6, default=None)
        size: protobug.UInt32 | None = protobug.field(7, default=None)

    @protobug.message
    class PackageInfo:
        packageid: protobug.UInt32 | None = protobug.field(1, default=None)
        change_number: protobug.UInt32 | None = protobug.field(2, default=None)
        missing_token: protobug.Bool | None = protobug.field(3, default=None)
        sha: protobug.Bytes | None = protobug.field(4, default=None)
        buffer: protobug.Bytes | None = protobug.field(5, default=None)
        size: protobug.UInt32 | None = protobug.field(6, default=None)

    apps: list[AppInfo] = protobug.field(1, default_factory=list)
    unknown_appids: list[protobug.UInt32] = protobug.field(2, default_factory=list)
    packages: list[PackageInfo] = protobug.field(3, default_factory=list)
    unknown_packageids: list[protobug.UInt32] = protobug.field(4, default_factory=list)
    meta_data_only: protobug.Bool | None = protobug.field(5, default=None)
    response_pending: protobug.Bool | None = protobug.field(6, default=None)
    http_min_size: protobug.UInt32 | None = protobug.field(7, default=None)
    http_host: protobug.String | None = protobug.field(8, default=None)
