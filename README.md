local development


install pyenv
select python 3.10 as default
install poetry
navigate to the project directory
poetry install
docker compose will create hte database for you
alembic upgrade head