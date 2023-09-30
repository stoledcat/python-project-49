install:
	poetry install


brain-games: 
	poetry run brain-games


build:
	rm dist/*.*
	poetry build


publish:
	poetry publish --dry-run


package-uninstall: 
	python3 -m pipx uninstall hexlet-code


package-install: 
	python3 -m pipx install dist/*.whl


make lint:
	poetry run flake8 brain_games
