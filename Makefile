install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run
#отладка пакета без публикации в каталог PyPI

package-install:
	python3 -m pip install --user dist/*.whl
#установка пакета из ОС(корневая директория проекта)

uninstall:
	pip uninstall hexlet_code

reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games
