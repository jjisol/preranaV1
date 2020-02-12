# instructor/urls.py
from django.urls import path
from . import views
from .models import Instructor

urlpatterns = [
    path('instructor_detail/<int:id>/', views.instructor_detail, name='instructor_detail'),
]
