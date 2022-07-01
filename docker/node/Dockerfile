ARG NODE_VERSION=16.13-slim

# define an alias for the specfic node version used in this file.
FROM node:${NODE_VERSION} as node

# Set Workdir
WORKDIR /usr/app

# Copy package files
COPY . .
COPY ./package-*.json .

# Install the project requirements.
RUN npm install esbuild
RUN npm install
RUN npm rebuild esbuild
RUN mkdir /usr/app/node_modules/.vite && chmod -R 777 /usr/app/node_modules/.vite

# Port used by this container to serve HTTP.
EXPOSE 3000
EXPOSE 9000

CMD ["npm", "run", "dev"]