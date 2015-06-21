from django.shortcuts import render
from django.http import HttpResponse

from authors.models import Author
from articles.models import Article

def index(request):
    return render(request, 'pages/index.html')

def acne_awareness(request):
    return render(request, 'pages/acne-awareness.html')

def celeb(request):
    return render(request, 'pages/celeb.html')

def hair(request):
    return render(request, 'pages/hair.html')

def nails(request):
    return render(request, 'pages/nails.html')

def makeup(request):
    return render(request, 'pages/makeup.html')

def skin(request):
    return render(request, 'pages/skin.html')

def view_article_by_slug(request, slug):
    article = Article.objects.get(slug=slug)
    return view_article(article.public_uuid)

def view_article(request, public_uuid):
    article = Article.objects.get(public_uuid=public_uuid)
    context = {
        'article': article,
        'content': article.content.splitlines(),
    }
    return render(request, 'pages/article.html', context)

def view_author(request, slug):
    author = Author.objects.get(slug=slug)
    context = {
        'author': author,
    }
    return render(request, 'pages/author.html', context)

## We're bypassing REST for the time being to render
## the article HTML on the server side.  What I would do
## for a two-day implementation is introduce a lightweight
## RESTful interface to fetch and search article, author, and
## tag data, write a small JavaScript API around such calls
## (perhaps with Backbone, but perhaps just a simple $.ajax
## wrapper), and introduce a top-level React.js SPA to stream-
## line display of the content.
##

def render_article_box(request, public_uuid):
    article = Article.objects.get(public_uuid=public_uuid)
    context = {
        'article': article,
    }
    return render(request, 'pages/partials/articlebox.html', context)
