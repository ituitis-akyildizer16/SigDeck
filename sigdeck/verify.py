"""Verification entry point."""

from . import ed25519


def verify_bytes(signature, message, public):
    try:
        return ed25519.verify(signature, message, public)
    except ValueError:
        return False


def verify_file(signature_path, file_path, public):
    sig = signature_path.read_bytes()
    if sig[:1] == b"-":
        from .armor import parse_signature
        sig = parse_signature(sig.decode("utf-8"))
    return verify_bytes(sig, file_path.read_bytes(), public)


def verify_dir(directory, public, suffix=".sig"):
    """Batch verify: every <file><suffix> in a directory."""
