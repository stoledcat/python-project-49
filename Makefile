#!/usr/bin/env python3

install:
	poetry install


brain-games:
	poetry run brain-games


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pipx install dist/*.whl
