import os
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from wq.db import rest
rest.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment to enable python-social-auth URLs
    # url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include(rest.router.urls))
)

if settings.DEBUG_WITH_RUNSERVER:
    urlpatterns.extend(patterns('',
        url(r'^media/', include('dmt.urls')), #debug mode only
    ))


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

if settings.DEBUG_WITH_RUNSERVER:
	# after building...
    urlpatterns += static('/css/', document_root=os.path.join(BASE_DIR, 'htdocs', 'css/'))
    urlpatterns += static('/images/', document_root=os.path.join(BASE_DIR, 'htdocs', 'images/'))
    urlpatterns += static('/js/', document_root=os.path.join(BASE_DIR, 'htdocs', 'js/'))
    urlpatterns += static('/', document_root=os.path.join(BASE_DIR, 'htdocs/'))
