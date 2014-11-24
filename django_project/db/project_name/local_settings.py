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

DEBUG = True
TEMPLATE_DEBUG = DEBUG
