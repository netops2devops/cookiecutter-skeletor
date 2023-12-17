lint: lint/bandit lint/black lint/autopep8

clean:
	docker compose down --remove-orphans --volumes
	@echo 'y' | docker system prune

build:
	docker compose build --no-cache

init:
	docker compose up --remove-orphans -d

stop:
	docker compose stop

lint/bandit:
	poetry run bandit -r src

lint/autopep8:
	poetry run autopep8 src tests

lint/black:
	poetry run black src tests

test:
	poetry run pytest
