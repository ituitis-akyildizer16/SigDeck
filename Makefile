PY ?= python3

.PHONY: test lint clean keygen

test:
	$(PY) -m pytest tests/ -o addopts=""

lint:
	$(PY) -m compileall -q sigdeck/

keygen:
	$(PY) -m sigdeck.cli keygen --out demo.key

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache/

<!-- draft note 882 -->
