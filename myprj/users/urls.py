from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getuser/', views.get_user, name='get_user'),
    path('adduser/', views.add_user, name='add_user'),
    path('adduser/addrecord/', views.add_record, name='add_record'),
    path('getuser/del_record/<int:id>', views.del_record, name='del_record'),
]