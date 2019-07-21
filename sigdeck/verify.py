"""Verification entry point."""

from . import ed25519


def verify_bytes(signature, message, public):
    try:
        return ed25519.verify(signature, message, public)
    except ValueError:
        return False


def verify_file(signature_path, file_path, public):
    sig = signature_path.read_bytes()
