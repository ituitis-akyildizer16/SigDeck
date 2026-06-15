# Keys and formats

- Secret keys: armored `SIGDECK SECRET KEY` blocks; the stored scalar is the
  clamped half of SHA-512 (RFC 8032) so loading and signing are one step.
- Public keys: armored `SIGDECK PUBLIC KEY` blocks, 32 bytes base64.
- Signatures: raw 64 bytes on disk, or armored `SIGDECK SIGNATURE` blocks
  with a CRC32 trailer for printer/copy survival.
- Optional passphrase: `sigdeck/scrypt_pw.py` seals the scalar with
  scrypt-derived key material (`n=2^14, r=8, p=1`).

## FAQ

Q: Can I reuse one key pair for everything? A: Yes, but a separate key per
project keeps a leaked file from compromising the rest of your signatures.

