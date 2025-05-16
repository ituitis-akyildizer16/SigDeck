"""Armored key round-trips."""

from sigdeck.keys import (armor_public, armor_secret, generate_seed, load_public,
                          load_secret, public_bytes)


def test_secret_roundtrip(tmp_path):
    seed = generate_seed()
    p = tmp_path / "k.key"
    p.write_text(armor_secret(seed, comment="test"), "utf-8")
