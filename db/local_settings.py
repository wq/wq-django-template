PROJECT_ROOT = "{{ project_directory }}"
STATIC_ROOT = PROJECT_ROOT + '/htdocs/static'
MEDIA_ROOT  = PROJECT_ROOT + '/media'
VERSION_TXT = PROJECT_ROOT + '/version.txt'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = "{{ secret_key }}"

TEMPLATE_DIRS = (
    PROJECT_ROOT + '/templates'
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
