# users/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('mypage/', views.mypage, name='mypage'),
    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),
    path('findUsername/', views.findUsername, name='findUsername'),
    path('findPassword/', views.findPassword, name='findPassword'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
]
