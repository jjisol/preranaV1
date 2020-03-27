from django.shortcuts import render, redirect, get_object_or_404
from .models import Center, CenterReview
from .filters import CenterFilter
from django.contrib import messages
from django.db.models import Q
from users.models import Cart
from .forms import CenterReviewForm
from django.core.paginator import Paginator

# Create your views here.
def intro(request):
    return render(request, 'center_intro.html', {})

def detail(request, id):
    center = get_object_or_404(Center, id=id)
    review = center.center_review.all()
    paginator = Paginator(review, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            return render(request, 'center_detail.html', {'center':center, 'cart':cart, 'page_obj':page_obj})
        else:
            return render(request, 'center_detail.html', {'center':center, 'page_obj':page_obj})
    except Exception as e:
        return render(request, 'center_detail.html', {'center':center, 'page_obj':page_obj})

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

def add_review_to_center(request, id):
    if request.user.is_authenticated:
        center = get_object_or_404(Center, id=id)
        if request.method == "POST":
            form = CenterReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.center = center
                review.author = request.user.username
                review.save()
                return redirect('center_detail', id=center.id)
            else:
                form = CenterReviewForm()
                messages.warning(request, "유효하지 않은 형식입니다. 다시 입력해주세요.")
                return render(request, 'add_review_to_center.html', {'form':form})
        else:
            form = CenterReviewForm()
            return render(request, 'add_review_to_center.html', {'form':form})
    else:
        messages.warning(request, "로그인 후 이용하실 수 있습니다.")
        return render(request, 'add_review_to_center.html', {'form':form})
