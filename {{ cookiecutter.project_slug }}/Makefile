lint: lint/bandit lint/black lint/isort lint/autopep8

clean:
	@echo 'y' | docker system prune

build:
	docker compose build --no-cache

start:
	docker compose up --remove-orphans -d

stop:
	docker compose stop

lint/bandit:
	poetry run bandit -r src

lint/isort:
	poetry run isort src tests

lint/autopep8:
	poetry run autopep8 src tests

lint/black:
	poetry run black src tests

test:
	poetry run pytest
