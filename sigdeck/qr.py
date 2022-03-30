"""QR payloads for moving keys and signatures across an air gap.

Payloads are text with an SGDK1: prefix so they survive phone cameras and
printers. The Android demo renders them with zxing; this module only
encodes and decodes the payload format.
"""

import base64

PREFIX = "SGDK1:"


def encode_key(public):
    body = base64.b32encode(public).decode("ascii").rstrip("=")
    return f"{PREFIX}key:{body}"

