"""Pure-Python Ed25519 (RFC 8032) - readable, stdlib-only, test-vector verified.

This is a from-scratch implementation kept deliberately small so it can be
audited on an air-gapped machine. It matches the RFC 8032 test vectors in
tests/test_ed25519.py.
"""

import hashlib

P = 2 ** 255 - 19
L = 2 ** 252 + 27742317777372353535851937790883648493
D = -121665 * pow(121666, P - 2, P) % P
I = pow(2, (P - 1) // 4, P)


def _inv(a):
    return pow(a, P - 2, P)


def _xrecover(y):
    xx = (y * y - 1) * _inv(D * y * y + 1) % P
    x = pow(xx, (P + 3) // 8, P)
    if (x * x - xx) % P:
        x = x * I % P
    if x % 2:
        x = P - x
    return x


_BY = 4 * _inv(5) % P
_BX = _xrecover(_BY)
B = (_BX, _BY)


def _encodepoint(point):
    x, y = point
    bits = [(y >> i) & 1 for i in range(255)] + [x & 1]
    return bytes(sum(bits[i * 8 + j] << j for j in range(8))
                 for i in range(32))


def _decodepoint(s):
    if len(s) != 32:
        raise ValueError("point must be 32 bytes")
    y = int.from_bytes(s, "little") & ((1 << 255) - 1)
    x = _xrecover(y)
    if x & 1 != (s[31] >> 7):
        x = P - x
    return (x, y)


def _point_add(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    x3 = (x1 * y2 + y1 * x2) * _inv(1 + D * x1 * x2 * y1 * y2) % P
    y3 = (y1 * y2 + x1 * x2) * _inv(1 - D * x1 * x2 * y1 * y2) % P
    return (x3, y3)


def _scalarmult(point, e):
    if e == 0:
        return (0, 1)
    q = _scalarmult(point, e >> 1)
    q = _point_add(q, q)
    if e & 1:
        q = _point_add(q, point)
    return q


def _scalarmult_base(e):
    return _scalarmult(B, e)


def public_key(seed):
    """32-byte seed -> 32-byte public key."""
    a, _ = _secret_expand(seed)
    return _encodepoint(_scalarmult_base(a))


