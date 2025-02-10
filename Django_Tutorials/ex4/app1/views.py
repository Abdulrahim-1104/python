from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Users

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        Users.objects.create(name=name, password=password)
        return redirect('/')  # Redirect to registrants page after successful regisrationt
    return render(request, 'register.html')

def registrants(request):
    users = Users.objects.all()
    return render(request, 'registrants.html', {'users': users})
