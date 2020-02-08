from django.shortcuts import render
from .models import OnedayClass
# Create your views here.
def class_detail(request, id):
    onedayclass = get_object_or_404(OnedayClass, id=id)
    return render(request, 'class_detail.html', {'onedayclass':onedayclass})
