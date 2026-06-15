# QR exchange

Payloads carry an `SGDK1:` prefix:

- `SGDK1:key:<base32 public key>` - 32 bytes
- `SGDK1:sig:<base32 signature>` - 64 bytes

Base32 keeps payloads short (no padding) and case-insensitive for
hand-typing. The Android demo scans them with zxing and the camera.
