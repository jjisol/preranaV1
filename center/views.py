from django.shortcuts import render, get_object_or_404
from .models import Center
from .filters import CenterFilter
from django.contrib import messages
from django.db.models import Q
from users.models import Cart

# Create your views here.
def intro(request):
    return render(request, 'center_intro.html', {})

def detail(request, id):
    center = get_object_or_404(Center, id=id)
    #instructors = Instructor.objects.filter(center=center.id)
    return render(request, 'center_detail.html', {'center':center, 'instructors':center})

def filter(request):
    center_list = Center.objects.all()
    center_filter = CenterFilter(request.GET, queryset=center_list)
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            return render(request, 'center_filter.html', {'filter':center_filter, 'cart':cart})
        else:
            return render(request, 'center_filter.html', {'filter':center_filter})
    except Exception as e:
        return render(request, 'center_filter.html', {'filter':center_filter})

def view_on_map(request):
    qs = Center.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(Q(address__icontains=q)|Q(name__icontains=q))

    return render(request, 'view_on_map.html', {'center_list':qs, 'q':q})
