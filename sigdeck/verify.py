"""Verification entry point."""

from . import ed25519


def verify_bytes(signature, message, public):
    try:
