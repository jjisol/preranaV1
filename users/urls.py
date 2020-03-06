# users/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('mypage/', views.mypage, name='mypage'),
    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),
    path('findUsername/', views.findUsername, name='findUsername'),
    path('findPassword/', views.findPassword, name='findPassword'),
	path('servicecenter/', views.service_center, name='service_center'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
    #cart
    path('cart/', views.cart_list, name='cart_list'),
    url(r'^add/(?P<id>\d+)/center/$', views.add_to_cart_center, name='add_to_cart_center'),
    url(r'^add/(?P<id>\d+)/event/$', views.add_to_cart_event, name='add_to_cart_event'),
    url(r'^add/(?P<id>\d+)/onedayclass/$', views.add_to_cart_onedayclass, name='add_to_cart_onedayclass'),
    url(r'^del/(?P<id>\d+)/center/$', views.del_from_cart_center, name='del_from_cart_center'),
    url(r'^del/(?P<id>\d+)/event/$', views.del_from_cart_event, name='del_from_cart_event'),
    url(r'^del/(?P<id>\d+)/onedayclass/$', views.del_from_cart_onedayclass, name='del_from_cart_onedayclass'),

]
