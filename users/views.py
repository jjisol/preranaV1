# users/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, DeleteAccountForm, CustomUserChangeForm
from .forms import LoginForm, FindUsernameForm, FindPasswordForm
from django.contrib.auth import login, authenticate
from .models import CustomUser, Cart
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['passwordCheck']:
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                email = form.cleaned_data.get("email")

                newUser = form.save(commit=False)
                newUser = CustomUser.objects.create_user(username=username, email=email, password=password)
                newUser.is_active = False
                newUser.save()

                current_site = get_current_site(request)
                mail_subject = 'PRERANA 회원가입 확인 메일'
                message = render_to_string('acc_active_email.html', {
                    'user': newUser,
                    'domain': current_site.domain,
                    'uid': force_text(urlsafe_base64_encode(force_bytes(newUser.id))),
                    'token': account_activation_token.make_token(newUser),
                })
                to_email = email
                emailmessage = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                emailmessage.send()
                form = CustomUserCreationForm()
                return render(request, 'signup.html', {'form':form, 'message':'회원가입을 완료하기 위해 이메일을 확인해주세요.'})
            else:
                form = CustomUserCreationForm()
                return render(request, 'signup.html', {'form':form, 'message':'비밀번호를 다시 확인해주세요.'})
        else:
            form = CustomUserCreationForm()
            return render(request, 'signup.html', {'form':form, 'message':'이미 존재하는 아이디거나 회원가입에 실패했습니다. 다시 입력해주세요.'})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'verification.html')

    return HttpResponse('이메일 인증 링크가 유효하지 않습니다.')


@csrf_exempt
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'message': '로그인에 실패했습니다. 다시 시도해주세요.', 'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def mypage(request):
    information = CustomUser.objects.get(username=request.user)
    return render(request, 'mypage.html', {'information':information})

@csrf_exempt
@login_required
def deleteAccount(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        try:
            if form.is_valid():
                password = form.cleaned_data['password']
                user = authenticate(request, username=request.user, password=password)
                if user is not None:
                    user.delete()
                    return redirect('home')
                else:
                    form = DeleteAccountForm()
                    return render(request, 'deleteAccount.html', {'message':'비밀번호가 일치하지 않습니다. 회원탈퇴에 실패했습니다.', 'form':form})
        except Exception as e:
            form = DeleteAccountForm()
            return render(request, 'deleteAccount.html', {'message':'비밀번호가 일치하지 않습니다. 회원탈퇴에 실패했습니다.', 'form':form})
    else:
        form = DeleteAccountForm()
        return render(request, 'deleteAccount.html', {'form':form})

@csrf_exempt
def findUsername(request):
    if request.method == 'POST':
        form = FindUsernameForm(request.POST)
        try:
            if form.is_valid():
                user = CustomUser.objects.get(email=form.cleaned_data['email'])
                if user is not None:
                    return render(request, 'findUsername.html', {'user':user})
        except Exception as e:
            form = FindUsernameForm()
            return render(request, 'findUsername.html', {'message':'입력하신 이메일은 등록되지 않은 이메일입니다. 다시 입력해주세요.', 'form':form})
    else:
        form = FindUsernameForm()
        return render(request, 'findUsername.html', {'form':form})

@csrf_exempt
def findPassword(request):
    if request.method == 'POST':
        form = FindPasswordForm(request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                user = CustomUser.objects.get(username=username, email=email)
                if user is not None:
                    current_site = get_current_site(request)
                    token = account_activation_token.make_token(user)
                    mail_subject = 'PRERANA에서 임시 비밀번호를 알려드립니다.'
                    message = render_to_string('password_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': force_text(urlsafe_base64_encode(force_bytes(user.id))),
                        'token': token,
                    })
                    to_email = email
                    emailmessage = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    emailmessage.send()
                    user.set_password(token)
                    user.save()
                    return render(request, 'password_email_confirm.html')

        except Exception as e:
            print(e)
            form = FindPasswordForm()
            return render(request, 'findPassword.html', {'message':'입력하신 정보와 일치하는 회원정보가 없습니다. 다시 입력해주세요.', 'form':form})
    else:
        form = FindPasswordForm()
        return render(request, 'findPassword.html', {'form':form})

@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('mypage')
        else:
            user_change_form = CustomUserChangeForm(instance = request.user)
            return render(request, 'editAccount.html', {'user_change_form':user_change_form})
    else:
	    user_change_form = CustomUserChangeForm(instance = request.user)
	    return render(request, 'editAccount.html', {'user_change_form':user_change_form})

@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)

        if password_change_form.is_valid():
            password_change_form.save()
            update_session_auth_hash(request, request.user)
            return redirect('mypage')
        else:
            password_change_form = PasswordChangeForm(request.user)
            return render(request, 'password.html', {'password_change_form':password_change_form})

    else:
        password_change_form = PasswordChangeForm(request.user)
        return render(request, 'password.html', {'password_change_form':password_change_form})
