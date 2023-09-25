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


# удаление установленного пакета проекта
package-uninstall: 
	python3 -m pipx uninstall hexlet-code


package-install-pip:
	python3 -m pip install --user dist/*.whl


package-install-pipx: 
	python3 -m pipx install dist/*.whl


# запуск линтера
make lint:
	poetry run flake8 brain_games