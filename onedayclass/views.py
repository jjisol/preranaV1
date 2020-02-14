from django.shortcuts import render
from .models import OnedayClass
from .filters import OnedayClassFilter
from .forms import OnedayClassFilterForm
# Create your views here.
def class_detail(request, id):
    onedayclass = get_object_or_404(OnedayClass, id=id)
    return render(request, 'class_detail.html', {'onedayclass':onedayclass})

def filter(request):
    onedayclass_list = OnedayClass.objects.all()
    filter = OnedayClassFilter(request.GET, queryset=onedayclass_list)

    return render(request, 'onedayclass_filter.html', {'filter':filter})
