#Makefile

install:
	sudo poetry install

brain-games:
	sudo poetry run brain-games

build:
	sudo poetry build

publish:
	sudo poetry publish --dry-run

package-install:
	sudo python3 -m pip install --user dist/*.whl

lint:
	sudo poetry run flake8 brain_games