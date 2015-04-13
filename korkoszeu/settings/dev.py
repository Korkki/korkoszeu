from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite.db')
    }
}

DEV_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

MIDDLEWARE_CLASSES = DEV_MIDDLEWARE_CLASSES + MIDDLEWARE_CLASSES

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
