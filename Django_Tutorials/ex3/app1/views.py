from django.shortcuts import render
from . import forms
# Create your views here.
def sendForm(request):
    form = forms.myForm()
    return render(request,'index.html',{'form':form})
