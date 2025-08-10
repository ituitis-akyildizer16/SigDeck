"""Signature armor round-trip and CRC guard."""

import pytest

from sigdeck.armor import ArmorError, armor_signature, parse_signature


def test_roundtrip():
    sig = bytes(range(64))
    text = armor_signature(sig)
    assert parse_signature(text) == sig


def test_crc_catches_corruption():
    sig = bytes(range(64))
    text = armor_signature(sig)
    # corrupt a byte in the base64 body - the CRC32 trailer must catch it
    broken = text.replace("AAEC", "AAED", 1)
    with pytest.raises(ArmorError):
        parse_signature(broken)
