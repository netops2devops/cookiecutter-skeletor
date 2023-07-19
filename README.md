# About 

This is a slightly opinionated yet simple `cookiecutter` template that generates boilerplate for a barebones python project which is ready to be used with the following: 

- `pytest`      for unit testing
- `bandit`      for security linting
- `Black`       for code formatting
- `autopep8`    for pep8 formatting
- [Poetry](https://python-poetry.org)   for package management
- [typer](http://typer.tiangolo.com)    for building CLI apps


# Requirements 

- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [poetry](https://python-poetry.org)

# Usage 

To setup a new python project with this cookiecutter
```
cookiecutter https://github.com/netops2devops/cookiecutter-skeletor.git
```

This generates a project structure as shown below. A git repository is automatically initialized upon project creation. As per best practices `.env` is created to store environment vars but is already put under `.gitignore`

```
❯ tree -a mypkg
mypkg
├── .env
├── .gitignore
├── .gitlab-ci.yml
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── README.md
├── docs
│   ├── develop.md
├── pyproject.toml
├── src
│   └── mypkg
│       ├── __init__.py
│       └── utils.py
└── tests
    └── test_utils.py
```
<br>

Finally, install the dependeneices in `pyproject.toml` under the new project root dir by running 
```
poetry install 
```

## To do

- Add Hashicorp Vault integration

## Author
Kapil Agrawal
