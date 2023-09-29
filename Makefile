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


package-install: 
	python3 -m pipx install dist/*.whl


# запуск линтера
make lint:
	poetry run flake8 brain_games
