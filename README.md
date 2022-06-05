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

.flake8 is used for flake8 linting