from django.conf.urls import include, url, static, patterns
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r'', include('pages.urls')),
    url(r'^article/', include('articles.urls')),

    # Included Django administrative pages.
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    )
