from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', ]

admin.site.register(CustomUser, CustomUserAdmin)
