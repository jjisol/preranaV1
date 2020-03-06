from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Notice
from .forms import NoticeForm
from django.contrib import messages
from django.core.paginator import Paginator

def notice_list(request):
    notices = Notice.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'notice_list.html', {'notices':notices})

def notice_detail(request, id):
    notice = get_object_or_404(Notice, id=id)
    return render(request, 'notice_detail.html', {'notice':notice})

def notice_new(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if request.user.is_staff:
            if form.is_valid():
                notice = form.save(commit=False)
                notice.author = request.user
                notice.published_date = timezone.now()
                notice.save()
                return redirect('notice_detail', id=notice.id)
            else:
                form = NoticeForm()
                return render(request, 'notice_edit.html',
                {'form':form, 'message':'글쓰기 권한이 없습니다.'})
        else:
            form = NoticeForm()
            return render(request, 'notice_edit.html',
            {'form':form, 'message':'글쓰기 권한이 없습니다.'})
    else:
        form = NoticeForm()
        return render(request, 'notice_edit.html', {'form':form})

def notice_edit(request, id):
    notice = get_object_or_404(Notice, id=id)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if request.user.is_staff:
            if form.is_valid():
                notice = form.save(commit=False)
                notice.author = request.user
                notice.published_date = timezone.now()
                notice.save()
                return redirect('notice_detail', id=notice.id)
            else:
                form = NoticeForm()
                return render(request, 'notice_edit.html',
                {'form':form, 'message':'권한이 없습니다.'})
        else:
            form = NoticeForm()
            return render(request, 'notice_edit.html',
             {'form':form, 'message':'권한이 없습니다.'})
    else:
        form = NoticeForm()
        return render(request, 'notice_edit.html', {'form':form})

def notice_remove(request, id):
    notice = get_object_or_404(Notice, id=id)
    notice.delete()
    return redirect('notice_list')
