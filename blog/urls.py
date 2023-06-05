from django.urls import path
from . import views

urlpatters = [
    path('', views.hello_world, name='hello_world'),
]