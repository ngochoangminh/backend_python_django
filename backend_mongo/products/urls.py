from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('new_product/', views.new_product, name='new_product'),
    path('new_product/add_product/',views.add_product,name='add_product'),
    path('delete/<str:_id>', views.delete, name='delete'),
]