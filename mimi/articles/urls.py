from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url('^(?P<public_uuid>[0-9a-f]{32})$', 'articles.views.view_article', name='articles-view-article'),
)
