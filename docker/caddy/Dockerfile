FROM abiosoft/caddy:latest

RUN mkdir -p /srv/www \
    /srv/caddy

WORKDIR /srv/caddy

ARG MKCERT_VERSION=1.4.3
RUN wget -O /usr/local/bin/mkcert https://github.com/FiloSottile/mkcert/releases/download/v${MKCERT_VERSION}/mkcert-v${MKCERT_VERSION}-linux-amd64
RUN chmod +x /usr/local/bin/mkcert

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && ln -s /usr/local/bin/docker-entrypoint.sh /
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

CMD ["/bin/parent", "caddy", "--agree=$ACME_AGREE"]
