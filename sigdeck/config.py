"""Shared settings."""

from pathlib import Path

DEFAULTS = {
    "key": "signing.key",
    "public": "signing.pub",
    "verify_dir": ".",
    "batch_suffix": ".sig",
}


def load_config(root="."):
    p = Path(root) / ".sigdeck.json"
    cfg = dict(DEFAULTS)
