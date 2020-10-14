from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('listjob/', views.listjob, name='listjob'),
]
