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
    if crc:
        crc32 = zlib.crc32(signature) & 0xFFFFFFFF
        lines.append(f"CRC32: {crc32:08x}")
    lines.append("")
    lines.append("\n".join(body[i:i + 64] for i in range(0, len(body), 64)))
    lines.append(END_SIG)
    return "\n".join(lines) + "\n"


def parse_signature(text):
    if BEGIN_SIG not in text or END_SIG not in text:
        raise ArmorError("not a SIGDECK signature block")
