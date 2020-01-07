"""ASCII armor for signatures (like PGP, minus the ego)."""

import base64
import zlib

BEGIN_SIG = "-----BEGIN SIGDECK SIGNATURE-----"
END_SIG = "-----END SIGDECK SIGNATURE-----"


class ArmorError(Exception):
    pass


def armor_signature(signature, crc=True):
    body = base64.b64encode(signature).decode("ascii")
    lines = [BEGIN_SIG]
