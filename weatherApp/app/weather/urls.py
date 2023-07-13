from django.urls import path
from . import views
from .views import add_city, delete_city, hourly_temperatures

urlpatterns = [
    path('', views.index, name='city_list'),  # URL pattern for the weather app's index view
    path('add/', add_city, name='add_city'),
    path('delete/', delete_city, name='delete_city'),
    path('hourly-temperatures/', views.hourly_temperatures, name='hourly_temperatures'),
    ]