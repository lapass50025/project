# 모듈 불러오기
from django.urls import path
from maps import views

app_name = "maps"

urlpatterns = [
    path('', views.index, name='index'),
]