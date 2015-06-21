from django.conf.urls import patterns, url

UUID_PATTERN = R'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

urlpatterns = patterns(
    '',

    url('^$', 'pages.views.index', name='index'),

    # Top-level pages.
    url('^acne-awareness/$', 'pages.views.acne_awareness', name='pages-acne-awareness'),
    url('^celeb/$', 'pages.views.celeb', name='pages-celeb'),
    url('^hair/$', 'pages.views.hair', name='pages-hair'),
    url('^nails/$', 'pages.views.nails', name='pages-nails'),
    url('^makeup/$', 'pages.views.makeup', name='pages-makeup'),
    url('^skin/$', 'pages.views.skin', name='pages-skin'),

    # Article-specific views.
    url('^article/(?P<public_uuid>{0})$'.format(UUID_PATTERN), 'pages.views.view_article', name='pages-view-article'),
    url('^article/(?P<slug>.+)$', 'pages.views.view_article_by_slug'),

    # Author-specific views.
    url('^author/(?P<slug>.+)$', 'pages.views.view_author', name='pages-view-author'),

    ## Server-side rendering calls.
    url('^render/articlebox/(?P<public_uuid>{0})$'.format(UUID_PATTERN), 'pages.views.render_article_box', name='pages-render-articlebox'),
)
