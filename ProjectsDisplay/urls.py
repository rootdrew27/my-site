from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectsIndex, name='ProjectsIndex'),
    path("<int:pk>/", views.ProjectDetail, name="ProjectDetail"),
]