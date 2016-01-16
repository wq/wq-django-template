import os
from django.conf.urls.static import static
from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from wq.db import rest
rest.autodiscover()

from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment to enable python-social-auth URLs
    # url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include(rest.router.urls))
]

if settings.DEBUG_WITH_RUNSERVER:

    # To use django-media-thumbnailer
    # urlpatterns.append(url('^media/', include('dmt.urls')))

    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

    # after building...
    urlpatterns += static(
        '/', document_root=os.path.join(settings.BASE_DIR, 'htdocs')
    )
