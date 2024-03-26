from .base import *

{% if with_gunicorn %}
import dj_database_url
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv("DEBUG") else False

ALLOWED_HOSTS = [os.getenv("WEBSITE_HOSTNAME") or "localhost"]
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {"default": dj_database_url.config()}

STORAGES = {
    "default": {
         # e.g. "storages.backends.s3.S3Storage"
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}
{% else %}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "{{ secret_key }}"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# wq: Determine if we are running off django's testing server
DEBUG_WITH_RUNSERVER = False

ALLOWED_HOSTS = ["{{ domain }}"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        {% if with_gis %}"ENGINE": "django.contrib.gis.db.backends.postgis",
        {% else %}"ENGINE": "django.db.backends.postgresql",
        # To enable GeoDjango:
        # "ENGINE": "django.contrib.gis.db.backends.postgis",
        {% endif %}"NAME": "{{ project_name }}",
        "USER": "{{ project_name }}",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}{% endif %}
