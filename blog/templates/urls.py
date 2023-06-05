from django.urls import path
from blog import views

urlpatters = [
    path('', views.hello_world, name='hello_world'),
]