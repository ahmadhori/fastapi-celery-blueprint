FROM python:3.9

WORKDIR /app

# install supervisord
RUN apt-get update && apt-get install -y supervisor

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY . /app

RUN poetry install

# run supervisord
CMD ["/usr/bin/supervisord"]