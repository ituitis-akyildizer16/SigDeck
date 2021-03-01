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
    head = text.split(BEGIN_SIG, 1)[1].split(END_SIG, 1)[0]
    crc = None
    chunks = []
    for line in head.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("CRC32:"):
            crc = line.split(":", 1)[1].strip()
            continue
        chunks.append(line)
    sig = base64.b64decode("".join(chunks))
    if crc and zlib.crc32(sig) & 0xFFFFFFFF != int(crc, 16):
        raise ArmorError("CRC32 mismatch - signature corrupt")
    return sig


def save_signature(path, signature):
    Path(path).write_text(armor_signature(signature), "utf-8")
