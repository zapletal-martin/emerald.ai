FROM python:3.11-bookworm

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml ./
RUN poetry install
RUN poetry lock --no-update
COPY ./ ./

EXPOSE 8087

WORKDIR /app/scripts

CMD ./start.sh
