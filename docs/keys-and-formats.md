# Keys and formats

- Secret keys: armored `SIGDECK SECRET KEY` blocks; the stored scalar is the
  clamped half of SHA-512 (RFC 8032) so loading and signing are one step.
- Public keys: armored `SIGDECK PUBLIC KEY` blocks, 32 bytes base64.
