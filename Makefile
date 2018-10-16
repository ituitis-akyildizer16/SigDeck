PY ?= python3

.PHONY: test lint clean keygen

test:
	$(PY) -m pytest tests/ -o addopts=""

lint:
