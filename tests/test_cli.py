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
    assert main(["keygen", "--out", str(key)]) == 0
    assert main(["pub", "--key", str(key), "--output", str(pub)]) == 0
    target = tmp_path / "a.bin"
    target.write_bytes(b"payload" * 50)
    sig = tmp_path / "a.bin.sig"