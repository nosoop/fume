#!/usr/bin/python3

import protobug


@protobug.message
class ContentManifestPayload:
    @protobug.message
    class FileMapping:
        @protobug.message
        class ChunkData:
            sha: protobug.Bytes | None = protobug.field(1, default=None)
            crc: protobug.Fixed32 | None = protobug.field(2, default=None)
            offset: protobug.UInt64 | None = protobug.field(3, default=None)
            cb_original: protobug.UInt32 | None = protobug.field(4, default=None)
            cb_compressed: protobug.UInt32 | None = protobug.field(5, default=None)

        filename: protobug.String | None = protobug.field(1, default=None)
        size: protobug.UInt64 | None = protobug.field(2, default=None)
        flags: protobug.UInt32 | None = protobug.field(3, default=None)
        sha_filename: protobug.Bytes | None = protobug.field(4, default=None)
        sha_content: protobug.Bytes | None = protobug.field(5, default=None)
        chunks: list[ChunkData] = protobug.field(6, default_factory=list)
        linktarget: protobug.String | None = protobug.field(7, default=None)

    mappings: list[FileMapping] = protobug.field(1, default=None)


@protobug.message
class ContentManifestMetadata:
    depot_id: protobug.UInt32 | None = protobug.field(1, default=None)
    gid_manifest: protobug.UInt64 | None = protobug.field(2, default=None)
    creation_time: protobug.UInt32 | None = protobug.field(3, default=None)
    filenames_encrypted: protobug.Bool | None = protobug.field(4, default=None)
    cb_disk_original: protobug.UInt64 | None = protobug.field(5, default=None)
    cb_disk_compressed: protobug.UInt64 | None = protobug.field(6, default=None)
    unique_chunks: protobug.UInt32 | None = protobug.field(7, default=None)
    crc_encrypted: protobug.UInt32 | None = protobug.field(8, default=None)
    crc_clear: protobug.UInt32 | None = protobug.field(9, default=None)


@protobug.message
class ContentManifestSignature:
    signature: protobug.Bytes | None = protobug.field(1, default=None)
