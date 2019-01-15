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
