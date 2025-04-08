install:
	uv sync

brain.games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

package-install:
	uv tool install dist/*.whl

run:
	uv run hexlet-python-packagemake

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

lint:
	uv run ruff check brain_games

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build