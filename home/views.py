from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView


def HomePageView(request):
    return render(request, 'home/home.html', {})

def introduction(request):
    return render(request, 'introduction.html', {})
