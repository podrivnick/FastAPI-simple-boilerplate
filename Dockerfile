FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

WORKDIR /FastAPI-simple-boilerplate

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends python3-dev \
                       gcc \
                       musl-dev \
                       libpq-dev \
                       nmap \
                       netcat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /FastAPI-simple-boilerplate

RUN pip install --upgrade --no-cache-dir pip==24.0 \
 && pip install --no-cache-dir poetry==1.8.2

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY ./config /FastAPI-simple-boilerplate/config
COPY ./src /FastAPI-simple-boilerplate/src

CMD ["python", "-Om", "src"]
