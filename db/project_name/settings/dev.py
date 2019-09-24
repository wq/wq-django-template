import os
import sys
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# wq: Determine if we are running off django's testing server
DEBUG_WITH_RUNSERVER = 'manage.py' in sys.argv[0]

{% if with_npm %}
if DEBUG_WITH_RUNSERVER:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'app', 'build', 'static')
    ]
{% endif %}

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        {% if with_gis %}'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        {% else %}'ENGINE': 'django.db.backends.sqlite3',
        # To enable GeoDjango:
        # 'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        {% endif %}'NAME': os.path.join(BASE_DIR, 'conf', '{{ project_name }}.sqlite3'),
    }
}

{% if not with_gis %}# {% endif %}SPATIALITE_LIBRARY_PATH = 'mod_spatialite.so'
