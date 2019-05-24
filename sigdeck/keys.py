"""Key generation, armored key files and loading."""

import base64
import os
from pathlib import Path

from . import ed25519
