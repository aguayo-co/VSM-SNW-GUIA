FROM node:16.16.0-bullseye-slim as node-build
# Set Workdir
WORKDIR /srv/app
# Copy app files
COPY . ./

# Install the project requirements.
RUN npm install
RUN mkdir -p static
RUN npm run build

FROM python:3.8.13-slim-bullseye as python-build

ARG DATABASE_URL=${DATABASE_URL}
ENV DATABASE_URL=${DATABASE_URL}

# Set working directory to function root directory
WORKDIR /srv/app
# Copy app files
COPY --from=node-build /srv/app/ ./

RUN apt-get update && apt-get install --no-install-recommends -y git curl postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Dependencies
RUN pip install -r requirements.txt
CMD ["sh","/srv/app/run_dev.sh"]
