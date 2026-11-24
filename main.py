#!/usr/bin/env python3
"""news-23 b55 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import hashlib
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1024 * 1024


def fail(msg):
    print("error: " + msg, file=sys.stderr)
    sys.exit(1)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        fail("MAKEFUN_OUTPUT_DIR is empty")
    out_dir = os.path.abspath(out_dir)
    if out_dir == os.path.abspath(HERE) or out_dir.startswith(os.path.abspath(HERE) + os.sep):
        fail("MAKEFUN_OUTPUT_DIR must not be inside the repo")
    if not os.path.isfile(SRC):
        fail("entry.png not found next to main.py")
    with open(SRC, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        fail("entry.png is %d bytes, over the 1 MiB limit" % len(data))
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        fail("entry.png is not a PNG file")
    width, height, depth, ctype = struct.unpack(">IIBB", data[16:26])
    if (width, height) != (1024, 1024):
        fail("entry.png is %dx%d, expected 1024x1024" % (width, height))
    if depth != 8 or ctype not in (2, 6):
        fail("unexpected PNG bit depth %d / colour type %d" % (depth, ctype))
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        fail("entry.png has a malformed IEND trailer")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        back = f.read()
    if back != data:
        fail("output differs from source")
    digest = hashlib.sha256(data).hexdigest()
    print("ok: wrote %s (%d bytes, %dx%d, sha256 %s)" % (dst, len(data), width, height, digest))
    print("source: entry.png (%d bytes, %dx%d, sha256 %s)" % (len(data), width, height, digest))
    print("verified: PNG signature + IHDR + IEND trailer + size limit, byte-identical copy")


if __name__ == "__main__":
    main()
