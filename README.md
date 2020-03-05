# cp-external-login Egg

## Build
```
$ python setup.py sdist
```

- In the machine where your django app runs
    - If installed --> `pip uninstall cp-external-login-egg`
    - To install -> `pip install --user cp-external-login-egg-0.1.zip`

## Django external authenticate method.

### INSTALLED_APPS
Add "cp_authentication" to your INSTALLED_APPS setting like this::
```
INSTALLED_APPS = (
    ...
    'cp_authentication',
)
```

### URLS
```
url(r'^external_login/', include('cp_authentication.urls')),
```


# Example configuration
To be added in django settings file.

```
#  external db login configuration

# -----------------------------------------------
#  external db login configuration

EXTERNAL_LOGIN_ACTIVE = True / False

EXTERNAL_DB_HOST = '127.0.0.1'
EXTERNAL_DB_PORT = 0
EXTERNAL_DB_SCHEMA = '***'
EXTERNAL_DB_USER = '***'
EXTERNAL_DB_PASSWORD = '***'

EXTERNAL_DB_TABLE = ''
EXTERNAL_DB_USERNAME_FIELD = '***'
EXTERNAL_DB_PASSWORD_FIELD = '***'

EXTERNAL_DB_ENGINE = 'django.db.backends.***'  # 'mysql', 'oracle', 'postgresql', 'sqlite3'
EXTERNAL_DB_HASH = '***'

if EXTERNAL_LOGIN_ACTIVE:
    external_database = {'ENGINE': EXTERNAL_DB_ENGINE, 'NAME': EXTERNAL_DB_SCHEMA, 'USER': EXTERNAL_DB_USER,
                         'PASSWORD': EXTERNAL_DB_PASSWORD, 'HOST': EXTERNAL_DB_HOST, 'PORT': EXTERNAL_DB_PORT}

    DATABASES['external_db'] = external_database
# -----------------------------------------------

```

