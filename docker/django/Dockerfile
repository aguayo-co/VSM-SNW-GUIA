# Python 'local' stage
FROM python:3.8.13-slim-bullseye as python-local-stage
RUN useradd wagtail

# 1. Force Python stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install OS requirements
RUN apt-get update && apt-get install --no-install-recommends -y git curl postgresql-client gettext \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
WORKDIR /root
RUN curl -sSL https://install.python-poetry.org/ | python3 -
ENV PATH="/root/.local/bin:${PATH}"

# Install the project requirements.
RUN poetry config virtualenvs.create false
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN PIP_NO_CACHE_DIR=false poetry install

# Setup EntryPoint
COPY ./docker/django/entrypoint /entrypoint
RUN chmod +x /entrypoint
ENTRYPOINT ["/entrypoint"]

# Port used by this container to serve HTTP.
EXPOSE 8000

# Serve Local
CMD ["python", "-Wd", "manage.py", "runserver", "--nostatic", "0.0.0.0:8000"]