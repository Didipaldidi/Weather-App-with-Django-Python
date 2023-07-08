from django.urls import path
from .views import register, user_login
from weather.views import index

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
