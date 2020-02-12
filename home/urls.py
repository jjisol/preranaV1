#home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('introduction/', views.introduction, name='introduction'),
]
