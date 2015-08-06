# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    if request.method == 'POST':
        csrfmiddlewaretoken = request.COOKIES.get('csrftoken', '')
        return HttpResponse(csrfmiddlewaretoken)
    elif request.method=='GET':
        return render_to_response('index.html')
    else:
        return HttpResponse('404')