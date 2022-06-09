# FastAPI/Celery Blueprint

This project is a blueprint for the a python webserver along side a celery worker to run background jobs, and it contains the follows:

- FastAPI as a webserver running using uvicorn
- Celery as a background job worker and scheduler.
- Redis is used as a borker and message queue.
- Postgres database is used as a result backend and it will store the results and the logs of the jobs.

Regarding the docker image it uses supervisor to run the celery worker and uvicorn webserver in one container image for the sake of running a simple application, for a more complicated setup you can still use the same docker image but you have to override the docker image entrypoint with your own command to run the webserver and celery worker each in a different container.
These commands are already included in the docker compose file and it also contains an example of how to run the webserver and celery worker in different containers (2 different services webserver + worker but they are already commented out).

## Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/)
* [Pyenv](https://github.com/pyenv/pyenv/)

## Local Development

* Install pyenv.

* Install python 3.9 using pyenv:

  ```bash
  pyenv install 3.9
  ```

* Set python 3.9 as default

  ```bash
  pyenv global 3.9
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

## Local Development Using Docker Compose

You can run the environment using docker compose (it takes sometime to build and download the dependencies and start up):

```bash
docker-compose up -d
```

Open the browser and navigate to http://0.0.0.0/docs to confirm that your server is up and running.

No need to build the project again after changeing the code if you don't add a new library as a new reuirenment.
you can just restart the docker container as follows and you will have your latest changes:

```bash
docker compose restart webserver_worker
```

To check the logs, run:

```bash
docker compose logs
```

To check the logs of a specific service, add the name of the service, e.g.:

```bash
docker compose logs -f webserver_worker
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
  