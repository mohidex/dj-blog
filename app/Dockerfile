FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN  apt-get update \
    && apt-get install -y --no-install-recommends \
        dumb-init \
        mime-support \
        libpq-dev \
        build-essential \
        libpoppler-cpp-dev \
        pkg-config \
        python-dev

COPY poetry.lock pyproject.toml ./
RUN pip3 install poetry
RUN poetry install

COPY . .

ENV STATIC_ROOT /app/static

RUN adduser --system --home /var/empty --shell /bin/nologin blogger \
    && addgroup --system blogger

EXPOSE 8000

USER blogger
