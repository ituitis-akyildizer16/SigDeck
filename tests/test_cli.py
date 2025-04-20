"""CLI-level smoke tests (argparse wiring, real files)."""

from sigdeck.cli import main


def test_keygen_writes_pair(tmp_path):
    key = tmp_path / "k.key"
    rc = main(["keygen", "--out", str(key)])
    assert rc == 0
    assert key.exists()
    assert key.with_suffix(".pub").exists()


def test_sign_then_verify(tmp_path):
    key = tmp_path / "k.key"
    pub = tmp_path / "k.pub"
