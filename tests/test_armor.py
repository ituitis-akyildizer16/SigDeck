"""Signature armor round-trip and CRC guard."""

import pytest

from sigdeck.armor import ArmorError, armor_signature, parse_signature


