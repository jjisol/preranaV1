# onedayclass/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('class_detail/<int:id>/', views.class_detail, name='class_detail'),
]
