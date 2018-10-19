PY ?= python3

.PHONY: test lint clean keygen

test:
	$(PY) -m pytest tests/ -o addopts=""

lint:
	$(PY) -m compileall -q sigdeck/

keygen:
	$(PY) -m sigdeck.cli keygen --out demo.key
