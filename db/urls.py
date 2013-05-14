from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from wq.db.rest import app
app.autodiscover()
app.router.add_page('index', {'url': ''})

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'',        include('social_auth.urls')),
    url(r'^',       include(app.router.urls))
)
