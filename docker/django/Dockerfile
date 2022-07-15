ARG PYTHON_VERSION=3.8.2-slim-buster

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python
# Add user that will be used in the container.
RUN useradd wagtail

# Python 'run' and 'build' stage
FROM python as python-run-stage

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages \
    build-essential \
    git \
    # psycopg2 dependencies \
    libpq-dev \
    curl \
    # wagtail and django dependencies \
    postgresql-client \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    libmagickwand-dev \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
WORKDIR /root
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="/root/.poetry/bin:${PATH}"

# Install Node
ARG NODE_VERSION=v16.13.0
ENV PATH="/root/node-${NODE_VERSION}-linux-x64/bin:${PATH}"
ENV NODE_NPX_PATH="/root/node-${NODE_VERSION}-linux-x64/bin/npx"
RUN curl -sSL "https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz" -O \
  && tar -xf node-${NODE_VERSION}-linux-x64.tar.xz \
  && npm config set unsafe-perm true && npm install -g npx --force

# Install the project requirements.
RUN poetry config virtualenvs.create false
COPY poetry.lock .
COPY pyproject.toml .
RUN PIP_NO_CACHE_DIR=false poetry install

# Setup EntryPoint
COPY ./docker/django/entrypoint /entrypoint
RUN chmod +x /entrypoint
ENTRYPOINT ["/entrypoint"]

WORKDIR /app
RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .

# Port used by this container to serve HTTP.
EXPOSE 8000

CMD ["python", "-Wd", "manage.py", "runserver", "--nostatic", "0.0.0.0:8000"]