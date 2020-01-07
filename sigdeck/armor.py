"""ASCII armor for signatures (like PGP, minus the ego)."""

import base64
import zlib

BEGIN_SIG = "-----BEGIN SIGDECK SIGNATURE-----"
END_SIG = "-----END SIGDECK SIGNATURE-----"

