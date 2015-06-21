from django.shortcuts import render

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
