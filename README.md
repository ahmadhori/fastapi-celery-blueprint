# FastAPI/Celery Blueprint

## Local Development

* Install pyenv.

* Install python 3.10 using pyenv:

  ```bash
  pyenv install 3.10.3
  ```

* Set python 3.10 as default

  ```bash
  pyenv global 3.10.3
  ```

* Install poetry

* Navigate to the project directory and install dependencies using poetry:

  ```bash
  poetry install
  ```

* docker compose will create the database for you

  ```bash
  docker-compose up
  ```

* upgrade the database:

  ```bash
  alembic upgrade head
  ```

---

## Linting and type checking

* `flake8` is used as first linter and its configuration is stored in the file `.flake8`
* `pylint` is used as second linter and its configuration is stored in the file `.pylintrc`
* `mypy` is enabled for type checking and the file `mypy.ini` contains the type checking configurations

## Formatting and sorting imports

* `autopep8` is enabled for auto formatting and its rules is in the file `.vscode/settings.json` - if you are using vscode then these rules will be applied automatically when formatting.
* `isort` is used to sort and clean the imports using the script `scripts/format-imports.sh` and you can run it  as follows:

  ```bash
  scripts/format-imports.sh
  ```
  