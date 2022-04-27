from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    template = loader.get_template('user_index.html')
    return HttpResponse(template.render())


def register(request):
    temp = loader.get_template('register.html')
    return HttpResponse(temp.render({}, request))

def add_user(request):
    name = request.POST['nameInput']
    phone = request.POST['phoneNumberInput']
    mail = request.POST['emailInput']
    pws  = request.POST['passwordInput']
    return HttpResponseRedirect(reverse('user'))

def update(request):
    return HttpResponse('request')

def profile(request):
    return HttpResponse('request')

def delete(request):
    return HttpResponse('request')