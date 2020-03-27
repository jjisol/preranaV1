from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import OnedayClass, OnedayClassReview

# Register your models here.
class OnedayClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'type', 'theme', 'date', 'day',
     'place', 'price']
    list_filter = [('date', DateRangeFilter),]
    search_fields = ['name']

class OnedayClassReviewAdmin(admin.ModelAdmin):
    list_display = ['onedayclass', 'author', 'text', 'created_date']
    search_fields = ['onedayclass', 'author']
    list_filter = (
        ('created_date', DateTimeRangeFilter),
    )

admin.site.register(OnedayClass, OnedayClassAdmin)
admin.site.register(OnedayClassReview, OnedayClassReviewAdmin)
