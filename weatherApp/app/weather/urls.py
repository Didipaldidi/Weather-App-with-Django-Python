from django.urls import path
from . import views
from .views import add_city, delete_city

urlpatterns = [
    path('', views.index, name='city_list'),
    path('add/', views.add_city, name='add_city'),
    path('delete/', views.delete_city, name='delete_city'),
]