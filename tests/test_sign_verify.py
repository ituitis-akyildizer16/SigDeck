"""End-to-end sign/verify with armored files."""

from sigdeck.keys import generate_seed, public_bytes
from sigdeck.sign import sign_file, detached_path
from sigdeck.verify import verify_file


def test_roundtrip(tmp_path):
    seed = generate_seed()
    target = tmp_path / "release.tar.gz"
    target.write_bytes(b"\x1f\x8b fake tarball bytes" * 100)
    sig = sign_file(target, seed)
    sig_path = tmp_path / detached_path(target).name
    sig_path.write_bytes(sig)
    assert verify_file(sig_path, target, public_bytes(seed))


def test_tampered_file(tmp_path):
    seed = generate_seed()
    target = tmp_path / "release.tar.gz"
    target.write_bytes(b"A" * 500)
    sig_path = tmp_path / detached_path(target).name
    sig_path.write_bytes(sign_file(target, seed))
    target.write_bytes(b"B" * 500)
    assert not verify_file(sig_path, target, public_bytes(seed))
