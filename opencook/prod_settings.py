from .settings import *
import dj_database_url

DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_ROOT = 'static'

DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['*']
