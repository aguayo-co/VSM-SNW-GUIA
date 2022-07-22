ARG NODE_VERSION=16.13-slim

# define an alias for the specfic node version used in this file.
FROM node:${NODE_VERSION} as node
# Set Workdir
WORKDIR /app

# Copy package files
COPY . .

# Install the project requirements.
RUN npm install
RUN npm run build

FROM python:3.8

ARG DATABASE_URL=${DATABASE_URL}
ENV DATABASE_URL=${DATABASE_URL}

# Set working directory to function root directory
WORKDIR /srv/app

RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages \
    build-essential \
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

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY --from=node /app /srv/app/

CMD sh /srv/app/run-dev.sh