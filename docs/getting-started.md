# Getting started

1. `pip install -e .` inside the repo (stdlib only - nothing else to fetch).
2. `sd keygen --out alice.key` - writes `alice.key` (secret) + `alice.pub`.
3. `sd sign release.tar.gz --key alice.key` - writes `release.tar.gz.sig`.
