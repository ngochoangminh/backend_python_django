from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import users

def index(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

# Show list username with jinja2
def get_user(request):
    temp = loader.get_template('profile.html')
    list_users = users.objects.all().values()
    contex =  {'users':list_users,}
    
    return  HttpResponse(temp.render(contex, request))


# call form add user and create new user record into database
def add_user(request):
    temp = loader.get_template('adduser.html')
    return HttpResponse(temp.render({}, request))

def add_record(request):
    # if request.method == 'POST':
    name = request.POST['usernameInput']
    pws  = request.POST['passwordInput']
    print(name, pws)
    # create new user
    users(username=name, password=pws).save()
    return HttpResponseRedirect(reverse('get_user'))

# Delete record
def del_record(request, id):
    users.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('get_user'))