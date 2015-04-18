from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'korkoszeu',
        'USER': 'rav'
    }
}

DEV_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

MIDDLEWARE_CLASSES = DEV_MIDDLEWARE_CLASSES + MIDDLEWARE_CLASSES

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
    }
}

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

COMPRESS = False

DEBUG_TOOLBAR_PATCH_SETTINGS = False
