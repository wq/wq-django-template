import sys
import mimetypes
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "{{ secret_key }}"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost"]{% if with_npm %}
CSRF_TRUSTED_ORIGINS = ["http://localhost:5173"]
{% else %}
# wq: Determine if we are running off django's testing server
DEBUG_WITH_RUNSERVER = "manage.py" in sys.argv[0]

if DEBUG_WITH_RUNSERVER:
    WQ_CONFIG_FILE = BASE_DIR / "app" / "js" / "data" / "config.js"{% endif %}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": {% if with_gis %}"django.contrib.gis.db.backends.postgis"{% else %}"django.db.backends.postgresql"{% endif %},
        "NAME": "{{ project_name }}",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    },
    # To use sqlite:
    # "default": {
    #     "ENGINE": {% if with_gis %}"django.contrib.gis.db.backends.spatialite"{% else %}"django.db.backends.sqlite3"{% endif %},
    #     "NAME": BASE_DIR / "conf" / "{{ project_name }}.sqlite3",
    # },
}

try:
    # Try to create dev database in container
    import psycopg2

    conn = psycopg2.connect(
        "host={HOST} user={USER}".format(**DATABASES["default"])
    )
    conn.set_session(autocommit=True)
    conn.cursor().execute(
        "CREATE DATABASE {NAME}".format(**DATABASES["default"])
    )
except Exception:
    pass
