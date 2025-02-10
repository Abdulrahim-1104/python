from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    sub = 'Mail from python django'
    msg = request.POST.get('message')
    receiver = [request.POST.get('receiver')]
    send_mail(sub,msg,'blacklover2311@gmail.com',receiver)
    return HttpResponse('<h1> Mail Sent Successfully </h1>')
# Create your views here.
