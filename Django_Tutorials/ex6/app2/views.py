from django.shortcuts import render

# Create your views here.
def sessions(request):

    #adding session
    request.session['key'] = 'value'

    #accessing session
    request.session['key']

    # deleting sessions
    del request.session['key']
