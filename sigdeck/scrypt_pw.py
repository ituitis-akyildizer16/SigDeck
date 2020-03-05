"""Passphrase sealing for secret keys (stdlib hashlib.scrypt)."""

import hashlib
import hmac
import os

N = 2 ** 14
R = 8
P = 1
DK_LEN = 32


def derive_key(passphrase, salt):
    """passphrase -> 32-byte key for key-file encryption."""
    return hashlib.scrypt(passphrase.encode("utf-8"), salt=salt,
                          n=N, r=R, p=P, dklen=DK_LEN)


def seal(secret, passphrase):
    """XOR the secret scalar with a derived key - simple, auditable."""
