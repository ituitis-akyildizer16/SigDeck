"""Passphrase sealing round-trip."""

from sigdeck.scrypt_pw import seal, unseal


def test_seal_roundtrip():
    secret = bytes(range(32))
    payload = seal(secret, "correct horse battery staple")
