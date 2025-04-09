"""Signature armor round-trip and CRC guard."""

import pytest

from sigdeck.armor import ArmorError, armor_signature, parse_signature


def test_roundtrip():
    sig = bytes(range(64))
    text = armor_signature(sig)
    assert parse_signature(text) == sig

