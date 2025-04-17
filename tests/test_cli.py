"""CLI-level smoke tests (argparse wiring, real files)."""

from sigdeck.cli import main


def test_keygen_writes_pair(tmp_path):
    key = tmp_path / "k.key"
