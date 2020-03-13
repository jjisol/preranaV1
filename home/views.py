from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView
from center.models import Center, CenterImage
from onedayclass.models import OnedayClass
from users.models import Cart

def HomePageView(request):
    centers = Center.objects.all().order_by('id')[:7]
    onedayclasses = OnedayClass.objects.all().order_by('id')[:7]
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            return render(request, 'home/home.html',
                {'centers':centers, 'onedayclasses':onedayclasses, 'cart':cart})
        else:
            return render(request, 'home/home.html',
                {'centers':centers, 'onedayclasses':onedayclasses})
    except Exception as e:
        return render(request, 'home/home.html',
            {'centers':centers, 'onedayclasses':onedayclasses})

def introduction(request):
    return render(request, 'introduction.html', {})

def yoga_detail(request):
    return render(request, 'yoga_detail.html', {})

def pilates_detail(request):
    return render(request, 'pilates_detail.html', {})
