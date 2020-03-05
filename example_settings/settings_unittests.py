from example_settings.settings import *

ALLOWED_HOSTS = ['*']

DJANGO_ENV = 'TESTS'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'default.sqlite3'),
    }
}
