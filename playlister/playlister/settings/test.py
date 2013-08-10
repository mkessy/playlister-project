from base import *
from os.path import join, normpath

########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"


########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "",
        "TEST_NAME": "test",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
