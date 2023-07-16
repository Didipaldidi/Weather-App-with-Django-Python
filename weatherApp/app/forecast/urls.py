from django.urls import path
from . import views

urlpatterns = [
    path('details/<str:city_name>/', views.details, name='details'),
]