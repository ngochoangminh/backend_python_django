from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='user'),
    path('register/', views.register, name='register'),
    path('register/adduser/',views.add_user, name='addrecord'),
    
]