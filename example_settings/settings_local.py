from example_settings.settings import *

ALLOWED_HOSTS = ['*']

DJANGO_ENV = 'LOCAL'

# -------------------------------------------------------------------------------------------------------------
#  external db login configuration

EXTERNAL_LOGIN_ACTIVE = False

EXTERNAL_DB_HOST = '127.0.0.1'
EXTERNAL_DB_PORT = 0
EXTERNAL_DB_SCHEMA = 'SCHEMA'
EXTERNAL_DB_USER = 'DB_USER'
EXTERNAL_DB_PASSWORD = 'DB_PASSWORD'

EXTERNAL_DB_TABLE = ''
EXTERNAL_DB_USERNAME_FIELD = 'USERNAME_FIELD'
EXTERNAL_DB_PASSWORD_FIELD = 'PASSWORD_FIELD'

EXTERNAL_DB_ENGINE = 'django.db.backends.mysql'  # 'mysql', 'oracle', 'postgresql', 'sqlite3'
EXTERNAL_DB_HASH = '***'

if EXTERNAL_LOGIN_ACTIVE:
    external_database = {'ENGINE': EXTERNAL_DB_ENGINE, 'NAME': EXTERNAL_DB_SCHEMA, 'USER': EXTERNAL_DB_USER,
                         'PASSWORD': EXTERNAL_DB_PASSWORD, 'HOST': EXTERNAL_DB_HOST, 'PORT': EXTERNAL_DB_PORT}

    DATABASES['external_db'] = external_database
# --------------------------------------------------------------------------------------------------------------
