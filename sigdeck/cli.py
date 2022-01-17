"""sd - the SigDeck command line interface."""

import argparse
import sys
from pathlib import Path

from .keys import (armor_public, armor_secret, generate_seed, load_public,
                   load_secret, save_armored)
from . import qr


