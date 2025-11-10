"""Signing entry point."""

from . import ed25519


def sign_bytes(message, seed):
    return ed25519.sign(message, seed)


def sign_file(path, seed):
    data = path.read_bytes()
    return sign_bytes(data, seed)


def detached_path(path):
    return path.with_suffix(str(path.suffix) + ".sig")
