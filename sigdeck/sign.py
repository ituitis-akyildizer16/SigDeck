"""Signing entry point."""

from . import ed25519


def sign_bytes(message, seed):
    return ed25519.sign(message, seed)


def sign_file(path, seed):
    data = path.read_bytes()
    return sign_bytes(data, seed)

