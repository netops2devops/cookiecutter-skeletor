lint: lint/bandit lint/black lint/isort lint/autopep8 lint/pre-commit

clean:
	@echo 'y' | docker system prune

build:
	docker compose build --no-cache

start:
	docker compose up --remove-orphans -d

stop:
	docker compose stop

lint/bandit:
	bandit -r src

lint/isort:
	isort src tests

lint/autopep8:
	autopep8 src tests

lint/black:
	black src tests

lint/pre-commit:
	pre-commit run -a 

test:
	pytest
