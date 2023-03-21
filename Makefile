#Makefile

install:
	sudo poetry install

brain-games:
	sudo poetry run brain-games

brain-even:
	sudo poetry run brain-even

brain-calc:
	sudo poetry run brain-calc

brain-gcd:
	sudo poetry run brain-gcd

brain-progression:
	sudo poetry run brain-progression

brain-prime:
	sudo poetry run brain-prime

build:
	sudo poetry build

publish:
	sudo poetry publish --dry-run

package-install:
	sudo python3 -m pip install --user dist/*.whl

lint:
	sudo poetry run flake8 brain_games