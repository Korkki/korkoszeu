from urllib.parse import urlparse
import dj_database_url

from .base import *

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
        'OPTIONS': {
            'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
            'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
        }
    }
}

redis_url = urlparse(os.environ.get('REDISCLOUD_URL'))

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = redis_url.hostname
SESSION_REDIS_PORT = redis_url.port
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = redis_url.password
SESSION_REDIS_PREFIX = 'session'

COMPRESS_ENABLED = True
