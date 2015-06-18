from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taskbuster_db',
        'USER': 'mazulo',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}
