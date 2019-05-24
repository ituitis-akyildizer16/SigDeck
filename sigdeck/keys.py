"""Key generation, armored key files and loading."""

import base64
import os
from pathlib import Path

from . import ed25519

ARMOR_PUB = "-----BEGIN SIGDECK PUBLIC KEY-----"
ARMOR_SEC = "-----BEGIN SIGDECK SECRET KEY-----"
ARMOR_END = "-----END SIGDECK {kind} KEY-----"

