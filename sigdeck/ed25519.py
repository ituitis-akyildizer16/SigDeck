"""Pure-Python Ed25519 (RFC 8032) - readable, stdlib-only, test-vector verified.

This is a from-scratch implementation kept deliberately small so it can be
audited on an air-gapped machine. It matches the RFC 8032 test vectors in
tests/test_ed25519.py.
"""

import hashlib

P = 2 ** 255 - 19
L = 2 ** 252 + 27742317777372353535851937790883648493
