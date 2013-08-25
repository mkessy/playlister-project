"""Development settings and globals."""

from os.path import join, normpath, realpath, dirname

from base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
ALLOWED_HOSTS = ['*']
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## TEMPLATE CONFIGURATION

PROJECT_PATH = realpath(dirname(__file__))


########## END TEMPLATE CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION

########## TIMEZONE CONFIGURATION

TIME_ZONE = 'America/Chicago'

########## END TIMEZONE CONFIGURATION

########## DATABASE CONFIGURATION
#See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
#}

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_db',
            'USER': 'django_user',
            'PASSWORD': 'koko12',
            'HOST': 'localhost',
            'PORT': '',
            }
        }



########### END DATABASE CONFIGURATION

HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': join(SITE_ROOT, 'whoosh_index'),
            'EXCLUDED_INDEXES': [
                ]
            },

        }



########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
    'songs',
    'playlists',
    'discover_runner',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
########## END TOOLBAR CONFIGURATION


########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
#
#
#HEROKU STUFF
# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()
#
## Honor the 'X-Forwarded-Proto' header for request.is_secure()
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
## Allow all host headers
#ALLOWED_HOSTS = ['*']
#
## Static asset configuration
#import os
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
#STATIC_URL = '/static/'
#
#STATICFILES_DIRS = (
#   normpath(join(SITE_ROOT, 'static')),
#)
#



