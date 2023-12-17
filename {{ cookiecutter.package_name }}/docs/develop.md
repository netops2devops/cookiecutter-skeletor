# Setup up a development environment

## Configure poetry
```
poetry config virtualenvs.in-project "true"
poetry config virtualenvs.path ".venv"
poetry config virtualenvs.prompt ".venv"
```

## Export environment variables
```
export $(cat .env | grep -v "#" | xargs)
```


## Install with development dependencies
```
poetry install --with=dev
```
