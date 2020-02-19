from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('notice/list/', views.notice_list, name='notice_list'),
    path('notice/<int:id>/', views.notice_detail, name='notice_detail'),
    path('notice/new', views.notice_new, name='notice_new'),
    path('notice/<int:id>/edit/', views.notice_edit, name='notice_edit'),
    url(r'^notice/(?P<id>\d+)/remove/$', views.notice_remove, name='notice_remove'),
]
