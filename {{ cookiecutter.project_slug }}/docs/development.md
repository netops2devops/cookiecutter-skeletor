## Setting up a development environment

#### Configure poetry to get control over it's virtualenv
```
poetry config virtualenvs.in-project "true"
poetry config virtualenvs.path ".venv"
poetry config virtualenvs.prompt ".venv"
```

#### To export env vars for local development
```
export $(cat .env | grep -v "#" | xargs)
```


#### To install development related dependencies 
```
poetry install --with=dev
```


