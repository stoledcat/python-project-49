#!/usr/bin/env python3

install:
	poetry install


brain-games: 
	poetry run brain-games


# сборка пакета
build:
	rm dist/*.*
	poetry build


# отладка публикации
publish:
	poetry publish --dry-run


# установка пакета из операционной системы. pipx указан из-за проблем c pip в Ubuntu 23.04
package-install: 
	python3 -m pipx install dist/*.whl


# запуск линтера
make lint:
	poetry run flake8 brain_games