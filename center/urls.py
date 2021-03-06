#center/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('intro/', views.intro, name='center_intro'),
    path('detail/<int:id>/', views.detail, name='center_detail'),
    path('filter/', views.filter, name='center_filter'),
    path('view_on_map/', views.view_on_map, name='view_on_map'),
    url(r'^review/(?P<id>\d+)/$', views.add_review_to_center, name='add_review_to_center'),
]
