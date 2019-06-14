"""Signing entry point."""

from . import ed25519


def sign_bytes(message, seed):
