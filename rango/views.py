from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("<a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("<a href='/rango/'>Index</a>")
