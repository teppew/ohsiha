from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> Website Homepage</h1>')


def about(request):
    return HttpResponse('<h1> Website About page</h1>')

# Create your views here.
