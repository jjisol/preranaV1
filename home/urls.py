#home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('introduction/', views.introduction, name='introduction'),
    path('yoga/datail/', views.yoga_detail, name='yoga_detail'),
    path('pilates/datail/', views.pilates_detail, name='pilates_detail'),
]
