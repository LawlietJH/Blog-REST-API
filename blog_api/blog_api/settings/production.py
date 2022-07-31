from .base import *

DEBUG = False
ALLOWED_HOSTS = ['deleonblogrestapi.herokuapp.com', 'lawlietjh.github.io']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
  'https://lawlietjh.github.io/',
)
