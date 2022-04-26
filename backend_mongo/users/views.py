from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def register(request):

    return HttpResponse('request')

def update(request):
    return HttpResponse('request')

def profile(request):
    return HttpResponse('request')

def delete(request):
    return HttpResponse('request')