from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# wq: Determine if we are running off django's testing server
DEBUG_WITH_RUNSERVER = False

ALLOWED_HOSTS = ["{{ domain }}"]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        {% if with_gis %}'ENGINE': 'django.contrib.gis.db.backends.postgis',
        {% else %}'ENGINE': 'django.db.backends.postgres',
        # To enable GeoDjango:
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        {% endif %}'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
