"""Batch release signing + verification."""

from sigdeck.batch import collect_release_files, sign_all
from sigdeck.keys import generate_seed, public_bytes
from sigdeck.verify import verify_dir


def test_batch(tmp_path):
