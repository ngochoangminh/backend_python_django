from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())

# Add new product
def new_product(request):
    return HttpResponse(request)

def add_product(request):
    return HttpResponseRedirect(reverse('products'))