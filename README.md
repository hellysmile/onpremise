# Sentry + rabbitmq + redis + nginx

## Up and Running

1. `mkdir -p data/{sentry,postgres,redis,rabbitmq,redis}`
2. `docker-compose up redis rabbitmq postgres`
3. `docker-compose run --rm web config generate-secret-key` - Generate a secret key.
    Add it to `docker-compose.yml` in `base` as `SENTRY_SECRET_KEY`.
4. `docker-compose run --rm web upgrade`
6. `docker-compose up -d`
7. Open `127.0.0.1:80`
