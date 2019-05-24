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
