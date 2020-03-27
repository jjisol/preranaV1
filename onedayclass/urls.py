# onedayclass/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('detail/<int:id>/', views.detail, name='onedayclass_detail'),
    path('filter/', views.filter, name='onedayclass_filter'),
    url(r'^review/(?P<id>\d+)/$', views.add_review_to_onedayclass, name='add_review_to_onedayclass'),
]
