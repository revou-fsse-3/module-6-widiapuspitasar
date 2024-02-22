FROM python:3.11-slim

RUN apt-get update && apt-get install -yq --no-install-recommends \
        libpq-dev \
        gcc \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install poetry

ENV POETRY_NO_INTERACTION=1 \
        POETRY_VIRTUALENVS_IN_PROJECT=1 \
        POETRY_VIRTUALENVS_CREATE=1 \
        POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install

COPY . /app

RUN poetry run flask db upgrade

CMD ["/app/.venv/bin/gunicorn","-w 4", "-b 0.0.0.0:5000", "app:app"]