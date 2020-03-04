from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cart

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', ]

class CartAdmin(admin.ModelAdmin):
    list_display=['user',]
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cart, CartAdmin)
