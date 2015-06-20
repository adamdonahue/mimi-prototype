from django.conf.urls import include, url, static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r'', include('pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
