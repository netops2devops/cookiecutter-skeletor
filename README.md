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

This generates a project structure as shown below. A git repository is automatically initialized upon project creation. As per best practices `.envs` dir is created to store environment vars but is already put under `.gitignore`
```
❯ tree -a mypkg
mypkg
├── .envs
│   ├── dev.env
│   └── prod.env
├── .gitignore
├── .gitlab-ci.yml
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── README.md
├── docs
│   ├── contributions.md
│   ├── install.md
│   └── intro.md
├── examples
│   └── example.py
├── pyproject.toml
├── pytest.ini
├── settings.cfg
├── src
│   └── mypkg
│       ├── __init__.py
│       └── utils.py
└── tests
    └── test_mypkg.py
```
<br>

Finally, install the dependeneices in `pyproject.toml` under the new project root dir by running 
```
poetry install 
```

## To do

- Template README, Makefile, CI file
- preconfigure linters
- Add Hashicorp Vault integration

## Authors
Kapil Agrawal
