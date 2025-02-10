from django.shortcuts import render

# Create your views here.
# dynamic content
def index(request):
    biodata = {'Name' : 'Abdul Rahim', 'Age' : 22 , 'DOB' : '11-11-2002'}
    data = {'bio':biodata}
    return render(request,'App2/index.html',context = data)
