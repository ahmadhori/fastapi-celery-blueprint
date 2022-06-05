## Local Development:

1. install pyenv

2. install python 3.10 using pyenv
`pyenv install 3.10.3`
3. set python 3.10 as default
`pyenv global 3.10.3`

4. install poetry

5. navigate to the project directory and install dependencies using poetry
`poetry install`

docker compose will create hte database for you
alembic upgrade head

## Linting and type checking

- flake8 is used as first linter and its configuration is stored in the file .flake8
- pylint is used as second linter and its configuration is stored in the file .pylintrc
- autopep8 is enabled for auto formatting and its rules is in the file .vscode/settings.json
- mypy is enabled for type checking and the file mypy.ini contains the type checking configurations
