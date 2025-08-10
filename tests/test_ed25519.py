"""RFC 8032 test vectors for the pure-python core."""

from sigdeck.ed25519 import public_key, sign, verify


def test_rfc8032_vector_1():
    seed = bytes.fromhex("9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60")
    pk = bytes.fromhex("d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a")
    sig = bytes.fromhex(
        "e5564300c360ac729086e2cc806e828a84877f1eb8e5d974d873e065224901555"
        "fb8821590a33bacc61e39701cf9b46bd25bf5f0595bbe24655141438e7a100b")
    assert public_key(seed) == pk
    assert sign(b"", seed) == sig
    assert verify(sig, b"", pk)


def test_rfc8032_vector_2():
    seed = bytes.fromhex("4ccd089b28ff96da9db6c346ec114e0f5b8a319f35aba624da8cf6ed4fb8a6fb")
    pk = bytes.fromhex("3d4017c3e843895a92b70aa74d1b7ebc9c982ccf2ec4968cc0cd55f12af4660c")
    msg = bytes([0x72])
    sig = bytes.fromhex(
        "92a009a9f0d4cab8720e820b5f642540a2b27b5416503f8fb3762223ebdb69da"
        "085ac1e43e15996e458f3613d0f11d8c387b2eaeb4302aeeb00d291612bb0c00")
    assert public_key(seed) == pk
    assert sign(msg, seed) == sig
    assert verify(sig, msg, pk)


def test_rfc8032_vector_3():
    seed = bytes.fromhex("c5aa8df43f9f837bedb7442f31dcb7b166d38535076f094b85ce3a2e0b4458f7")
    pk = bytes.fromhex("fc51cd8e6218a1a38da47ed00230f0580816ed13ba3303ac5deb911548908025")
    msg = bytes.fromhex("af82")
    sig = bytes.fromhex(
        "6291d657deec24024827e69c3abe01a30ce548a284743a445e3680d7db5ac3ac"
        "18ff9b538d16f290ae67f760984dc6594a7c15e9716ed28dc027beceea1ec40a")
    assert public_key(seed) == pk
    assert sign(msg, seed) == sig
    assert verify(sig, msg, pk)


def test_tamper_detected():
    seed = bytes.fromhex("9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60")
    pk = public_key(seed)
    sig = sign(b"hello", seed)
    assert verify(sig, b"hello", pk)
    assert not verify(sig, b"hellp", pk)
    bad = bytearray(sig); bad[0] ^= 1
    assert not verify(bytes(bad), b"hello", pk)
