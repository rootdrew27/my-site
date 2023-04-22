from django.urls import path

from . import views

#namespace for html url tags (template tags)
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #eg: /polls/2/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #eg: /polls/2/results/
    path('<int:question_id>/vote', views.vote, name='vote'),
    #eg: /polls/2/vote/
]