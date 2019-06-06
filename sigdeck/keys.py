"""Key generation, armored key files and loading."""

import base64
import os
from pathlib import Path

from . import ed25519

ARMOR_PUB = "-----BEGIN SIGDECK PUBLIC KEY-----"
ARMOR_SEC = "-----BEGIN SIGDECK SECRET KEY-----"
ARMOR_END = "-----END SIGDECK {kind} KEY-----"


class KeyError2(Exception):
    pass


def generate_seed():
    return os.urandom(32)


def public_bytes(seed):
    return ed25519.public_key(seed)


def _wrap(b64, width=64):
    return "\n".join(b64[i:i + width] for i in range(0, len(b64), width))


def armor_public(public, comment=""):
    lines = [ARMOR_PUB]
    if comment:
        lines.append(f"Comment: {comment}")
    lines.append("")
    lines.append(_wrap(base64.b64encode(public).decode("ascii")))
    lines.append(ARMOR_END.replace("{kind}", "PUBLIC"))
    return "\n".join(lines) + "\n"


def armor_secret(seed, comment=""):
    body = base64.b64encode(seed).decode("ascii")
    lines = [ARMOR_SEC]
    if comment:
        lines.append(f"Comment: {comment}")
    lines.append("")
    lines.append(_wrap(body))
    lines.append(ARMOR_END.replace("{kind}", "SECRET"))
    return "\n".join(lines) + "\n"
