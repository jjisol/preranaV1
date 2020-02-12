from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from .models import OnedayClass

# Register your models here.
class OnedayClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'type', 'theme', 'date', 'day',
     'place', 'price']
    list_filter = [('date', DateRangeFilter),]
    search_fields = ['name']

admin.site.register(OnedayClass, OnedayClassAdmin)
