from django.shortcuts import render, get_object_or_404
from .models import OnedayClass
from .filters import OnedayClassFilter
from .forms import OnedayClassFilterForm
from users.models import Cart

def detail(request, id):
    onedayclass = get_object_or_404(OnedayClass, id=id)
    return render(request, 'onedayclass_detail.html', {'onedayclass':onedayclass})

def filter(request):
    onedayclass_list = OnedayClass.objects.all()
    filter = OnedayClassFilter(request.GET, queryset=onedayclass_list)
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        return render(request, 'onedayclass_filter.html', {'filter':filter, 'cart':cart})
    else:
        return render(request, 'onedayclass_filter.html', {'filter':filter})
