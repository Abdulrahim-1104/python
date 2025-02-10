from django.shortcuts import render

# Create your views here.
def cookies(request):
    response = render(request,'index.html')
    username = 'Abdul rahim'
    # setting cookies
    response.set_cookie('username',username)
    # accessing cookies
    request.COOKIES.get('username')
    # deleting cookies
    response.delete_cookie('username')

