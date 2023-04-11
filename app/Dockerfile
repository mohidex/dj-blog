FROM python:3.8-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
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

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV STATIC_ROOT /app/static

RUN adduser --system --home /var/empty --shell /bin/nologin blogger \
    && addgroup --system blogger

EXPOSE 8000

USER blogger
