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
ENV SECRET_KEY=${SECRET_KEY}
ENV DATABASE_URL=${DATABASE_URL}

# Copy app files
COPY --from=node-build /srv/app/ /srv/app

# Set working directory to function root directory
WORKDIR /srv/app

RUN apt-get update && apt-get install --no-install-recommends -y git curl postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Dependencies
RUN pip install -r requirements.txt
RUN python manage.py migrate --noinput
RUN python manage.py compilescss --use-storage
RUN python manage.py collectstatic --no-input
CMD ["python", "-Wd", "manage.py", "runserver", "--nostatic", "0.0.0.0:8000"]
