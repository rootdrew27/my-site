from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogIndex, name='BlogIndex'),
    path('<int:pk>/', views.BlogDetail, name='BlogDetail'),
    path('<category>/', views.BlogCategory, name='BlogCategory')
]