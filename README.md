# About 

This is a slightly opinionated yet simple `cookiecutter` template for my personal use that generates a barebone python project ready to be used with the following: 

- `Black`     for code formatting
- `pytest`    for unit testing
- `Poetry`    for package management
- `coverage`  for test coverage reporting
- `flake8`    for code linting
- `mypy`      for type checking
- [Typer](http://typer.tiangolo.com) for building CLI apps
- [bandit](https://github.com/PyCQA/bandit) for security linting

# Requirements 

- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [poetry](https://python-poetry.org)

# Usage 

Setup a new skeleton python barebones project 
```
cookiecutter https://github.com/netops2devops/cookiecutter-skeletor.git
```

This generates a project structure as shown below
```
❯ tree -a mytestproject
mytestproject
├── .gitignore
├── .gitlab-ci.yml
├── Dockerfile
├── Makefile
├── README.md
├── docker-compose.yml
├── docs/
├── examples/
├── pyproject.toml
├── src
│   ├── mytestproject
│   │   └── __init__.py
│   └── utils
│       ├── __init__.py
│       └── helper.py
├── tests/
└── tox.ini
```
<br>

Finally, install the dependeneices in `pyproject.toml` under the new project root dir by running 
```
poetry install 
```

## To do

- Add `post_gen_project` hooks to further customize layout based on user input
    - generate CI file(s) based on user choice (github vs. gitlab)
    - auto initialize a git repo (with base git config) upon project creation
- Template README, Makefile, CI file
- preconfigure linters
- Add Hashicorp Vault integration

## Authors
Kapil Agrawal
