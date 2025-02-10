from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1> Welcome to App 2</h2>')

def rahim(request):
    return HttpResponse('<h1> This is Abdul Rahim Url</h2>')

def jasra(request):
    return HttpResponse('<h1> This is Jasra Url</h2>')
# Create your views here.
