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


def encode_signature(signature):
    body = base64.b32encode(signature).decode("ascii").rstrip("=")
    return f"{PREFIX}sig:{body}"


def decode(payload):
    if not payload.startswith(PREFIX):
        raise ValueError("not a SigDeck payload")
    kind, _, body = payload[len(PREFIX):].partition(":")
    if kind not in ("key", "sig"):
        raise ValueError(f"unknown payload kind {kind!r}")
    pad = "=" * ((8 - len(body) % 8) % 8)
