from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from wq.db import rest
rest.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include(rest.router.urls))
)
