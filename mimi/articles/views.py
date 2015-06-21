from django.http import HttpResponse
from django.shortcuts import render

def view_article(request, public_uuid):
    return HttpResponse("Would display article %s" % public_uuid)
