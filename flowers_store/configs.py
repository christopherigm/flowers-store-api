import os
from pathlib import Path
import environ


BASE_DIR=Path(__file__).resolve().parent.parent

environment=environ.Env(
    SECRET_KEY=(str, 'key'),
    ENVT=(str, 'localhost'),
    DB_NAME=(str, 'flowers-store-api'),
    DB_USER=(str, 'flowers-store-api'),
    DB_PASSWORD=(str, 'flowers-store-api'),
    EMAIL_HOST_USER=(str, 'john@doe.com'),
    EMAIL_HOST_PASSWORD=(str, 'password'),
    OP_API_KEY=(str, 'my-key'),
    OP_MERCHANT_ID=(str, 'my-id'),
)

environ.Env.read_env()


SECRET_KEY=environment('SECRET_KEY')
ENVT=environment('ENVT')
DB_NAME=environment('DB_NAME')
DB_USER=environment('DB_USER')
DB_PASSWORD=environment('DB_PASSWORD')
EMAIL_HOST_USER=environment('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=environment('EMAIL_HOST_PASSWORD')
OP_API_KEY=environment('OP_API_KEY')
OP_MERCHANT_ID=environment('OP_MERCHANT_ID')


class Common:
    SECRET_KEY=SECRET_KEY
    SITE_HEADER='Flowers Store CMS'
    INDEX_TITLE='CMS'
    SITE_TITLE='CMS'
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_USE_TLS=True
    EMAIL_PORT=587
    DEBUG=True
    ALLOWED_HOSTS=['*']
    JWT_ACCESS_EXPIRATION_DAYS=360
    JWT_REFRESH_EXPIRATION_DAYS=360
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': 'flowers-store-api-db',
            'PORT': '5432'
        }
    }
    EMAIL_HOST_USER=EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD
    ENVT=ENVT
    MEDIA_ROOT='/media'
    STATIC_ROOT='/static'
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    OP_API_KEY=OP_API_KEY
    OP_MERCHANT_ID=OP_MERCHANT_ID
    OP_VERIFY_SSL_CERTS=False
    OP_PRODUCTION=False


class LOCAL(Common):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }
    WEB_APP_URL='http://127.0.0.1:3000/'
    API_URL='http://127.0.0.1:8000/'
    MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')


class STAGING(Common):
    WEB_APP_URL='https://flowers-store.iguzman.com.mx/'
    API_URL='https://api.flowers-store.iguzman.com.mx/'


class MASTER(Common):
    DEBUG=False
    JWT_ACCESS_EXPIRATION_DAYS=30
    JWT_REFRESH_EXPIRATION_DAYS=360
    OP_VERIFY_SSL_CERTS=True
    OP_PRODUCTION=True
    WEB_APP_URL='https://www.flowers-store.com/'
    API_URL='https://api.flowers-store.com/'


if ENVT == 'staging':
    env=STAGING
elif ENVT == 'master':
    env=MASTER
else:
    env=LOCAL
