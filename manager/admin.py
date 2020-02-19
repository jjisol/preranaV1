from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
     list_display = ['author', 'title', 'created_date', 'published_date',]
     search_fields = ['title',]
admin.site.register(Notice, NoticeAdmin)
