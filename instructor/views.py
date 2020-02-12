from django.shortcuts import render
from .models import Instructor
# Create your views here.
def instructor_detail(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    return render(request, 'instructor_detail.html', {'instructor':instructor})
