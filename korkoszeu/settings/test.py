from .prod import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': os.environ.get('PG_USER'),
        'PASSWORD': os.environ.get('PG_PASSWORD'),
        'HOST': '127.0.0.1',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = 'password'
SESSION_REDIS_PREFIX = 'session'
