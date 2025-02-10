from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Hello Mother Fucker </h>')

def index(request):
    return HttpResponse('<h1> Welcome Home </h>')

# Create your views here.
