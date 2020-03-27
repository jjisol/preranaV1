from django.shortcuts import render, redirect, get_object_or_404
from .models import OnedayClass, OnedayClassReview
from .filters import OnedayClassFilter
from .forms import OnedayClassReviewForm
from users.models import Cart
from django.core.paginator import Paginator

def detail(request, id):
    onedayclass = get_object_or_404(OnedayClass, id=id)
    review = onedayclass.onedayclass_review.all()
    paginator = Paginator(review, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            return render(request, 'onedayclass_detail.html', {'onedayclass':onedayclass, 'cart':cart, 'page_obj':page_obj})
        else:
            return render(request, 'onedayclass_detail.html', {'onedayclass':onedayclass, 'page_obj':page_obj})
    except Exception as e:
        return render(request, 'onedayclass_detail.html', {'onedayclass':onedayclass, 'page_obj':page_obj})

def add_review_to_onedayclass(request, id):
    if request.user.is_authenticated:
        onedayclass = get_object_or_404(OnedayClass, id=id)
        if request.method == "POST":
            form = OnedayClassReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.onedayclass = onedayclass
                review.author = request.user.username
                review.save()
                return redirect('onedayclass_detail', id=onedayclass.id)
            else:
                form = OnedayClassReviewForm()
                messages.warning(request, "유효하지 않은 형식입니다. 다시 입력해주세요.")
                return render(request, 'add_review_to_onedayclass.html', {'form':form})
        else:
            form = OnedayClassReviewForm()
            return render(request, 'add_review_to_onedayclass.html', {'form':form})
    else:
        messages.warning(request, "로그인 후 이용하실 수 있습니다.")
        return render(request, 'add_review_to_center.onedayclass', {'form':form})


def filter(request):
    onedayclass_list = OnedayClass.objects.all()
    filter = OnedayClassFilter(request.GET, queryset=onedayclass_list)
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            return render(request, 'onedayclass_filter.html', {'filter':filter, 'cart':cart})
        else:
            return render(request, 'onedayclass_filter.html', {'filter':filter})
    except Exception as e:
            return render(request, 'onedayclass_filter.html', {'filter':filter})
