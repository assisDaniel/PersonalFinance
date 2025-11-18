import os
from .base import *

#
DEBUG = False
#
ALLOWED_HOSTS = []
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = []
CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}