from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url('^$', 'pages.views.index', name='index'),
)
