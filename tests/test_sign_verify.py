"""End-to-end sign/verify with armored files."""

from sigdeck.keys import generate_seed, public_bytes
from sigdeck.sign import sign_file, detached_path
from sigdeck.verify import verify_file


def test_roundtrip(tmp_path):
    seed = generate_seed()
