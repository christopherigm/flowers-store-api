FROM python:3.9.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SECRET_KEY={FLOWERS_STORE_API_SECRET_KEY} \
    ENVT={FLOWERS_STORE_API_ENVIRONMENT} \
    DB_NAME={FLOWERS_STORE_API_POSTGRES_DB} \
    DB_USER={FLOWERS_STORE_API_POSTGRES_USER} \
    DB_PASSWORD={FLOWERS_STORE_API_POSTGRES_PASSWORD} \
    EMAIL_HOST_USER={FLOWERS_STORE_API_EMAIL_HOST_USER} \
    EMAIL_HOST_PASSWORD={FLOWERS_STORE_API_EMAIL_HOST_PASSWORD}

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD [ "/bin/sh", "docker-entrypoint.sh" ]