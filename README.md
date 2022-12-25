# About 

This is a slightly opinionated yet simple `cookiecutter` template that will generate a barebones python project ready to be used with the following: 

- `Black` linter
- `pytest` for unit testing
- `Poetry` for package management
- `Docker` and `docker-compose`
- `Makefile`
- `Typer` for cli builder
- `bandit` for security linter

# Requirements 

- cookiecutter
- poetry 

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
├── dev
│   ├── Dockerfile
│   ├── development.md
│   └── docker-compose.yml
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

# To do
Add some post_gen hooks to further customize layout based on user input. 

# Author
Kapil Agrawal
