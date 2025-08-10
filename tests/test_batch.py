"""Batch release signing + verification."""

from sigdeck.batch import collect_release_files, sign_all
from sigdeck.keys import generate_seed, public_bytes
from sigdeck.verify import verify_dir


def test_batch(tmp_path):
    (tmp_path / "app-v1.tar.gz").write_bytes(b"app" * 100)
    (tmp_path / "app-v1.tar.gz.sig").write_bytes(b"junk")
    (tmp_path / "README.txt").write_bytes(b"readme")
    files = collect_release_files(tmp_path)
    assert {f.name for f in files} == {"app-v1.tar.gz", "README.txt"}