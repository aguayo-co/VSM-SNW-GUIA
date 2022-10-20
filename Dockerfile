FROM node:16.16.0-bullseye-slim as node-build

# Copy app files
COPY . /srv/app

# Set Workdir
WORKDIR /srv/app

# Install the project requirements.
RUN npm install
RUN mkdir -p static
RUN npm run build

FROM python:3.8.13-slim-bullseye as python-build

ARG DATABASE_URL=${DATABASE_URL}
ARG SECRET_KEY=${SECRET_KEY}
ARG DJANGO_VITE_DEV_MODE=${DJANGO_VITE_DEV_MODE}
ENV SECRET_KEY=${SECRET_KEY}
ENV DATABASE_URL=${DATABASE_URL}
ENV DJANGO_VITE_DEV_MODE=${DJANGO_VITE_DEV_MODE}

# Copy app files
COPY --from=node-build /srv/app/ /srv/app

# Set working directory to function root directory
WORKDIR /srv/app

RUN apt-get update && apt-get install --no-install-recommends -y git curl postgresql-client gettext \
    && rm -rf /var/lib/apt/lists/*

# Install Dependencies
RUN pip install -r requirements.txt
RUN chmod +x /srv/app/run_dev.sh
RUN git pull
CMD ["sh","/srv/app/run_dev.sh"]
