from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url('^$', 'pages.views.index', name='index'),

    url('^acne-awareness/$', 'pages.views.acne_awareness', name='pages-acne-awareness'),
    url('^celeb/$', 'pages.views.celeb', name='pages-celeb'),
    url('^hair/$', 'pages.views.hair', name='pages-hair'),
    url('^nails/$', 'pages.views.nails', name='pages-nails'),
    url('^makeup/$', 'pages.views.makeup', name='pages-makeup'),
    url('^skin/$', 'pages.views.skin', name='pages-skin'),

)
