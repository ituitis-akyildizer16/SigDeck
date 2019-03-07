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
