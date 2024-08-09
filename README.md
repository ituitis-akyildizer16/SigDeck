# SigDeck

![ci-python](https://github.com/ituitis-akyildizer16/SigDeck/actions/workflows/ci-python.yml/badge.svg)
![license](https://img.shields.io/badge/license-MIT-blue.svg)
![python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![air-gapped](https://img.shields.io/badge/air--gapped-yes-green.svg)

**Offline Ed25519 signing toolkit** - sign files, verify signatures, exchange
keys via QR. Fully air-gapped: a pure-Python RFC 8032 implementation, scrypt
passphrases, and ASCII armor. The signing playground for people who don't
trust their clipboard.

## Why this exists

I wanted a signing tool I could run on a machine with no network at all - no
pip downloads, no telemetry, no cloud. SigDeck is a single Python package with
a from-scratch Ed25519 core, a passphrase-wrapped secret key format, and QR
payloads for moving keys and signatures across an air gap.

## Layout

```
sigdeck/    the Python engine (pure stdlib: keys, sign, verify, armor, qr)
app/        minimal Android demo: scan QR keys, sign, verify
docs/       guides (getting started, formats, qr exchange, shortcuts)
examples/   end-to-end recipes (signing releases, qr verification)
```

## Quick start

```console
$ pip install -e .
$ sd keygen --out alice.key
$ sd pub alice.key --output alice.pub
$ sd sign release.tar.gz --key alice.key
$ sd verify release.tar.gz --sig release.tar.gz.sig --pub alice.pub
Verified
```

## The signing playground rules

- **Pure stdlib** - the whole engine uses `hashlib`, `hmac`, `base64`, `os`,
  `zlib`. Nothing to download, ever.
- **Ed25519 from scratch** - RFC 8032, test-vector verified (see tests).
- **Passphrase option** - secret keys can be sealed with scrypt
  (`hashlib.scrypt`) so a stolen key file is still useless.
- **QR exchange** - `SGDK1:` payloads carry public keys and signatures
  across air gaps (print, scan, done).

## Requirements

- Python 3.9+ (no third-party dependencies for the engine)
- Android Studio for the demo app

## Contributing

PRs welcome - see [CONTRIBUTING.md](CONTRIBUTING.md). `make test` before push;
CI mirrors it.

## License

MIT - see [LICENSE](LICENSE).

<!-- draft note 616 -->
