"""Passphrase sealing for secret keys (stdlib hashlib.scrypt)."""

import hashlib
import hmac
import os

N = 2 ** 14
R = 8
P = 1
