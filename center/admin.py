from django.contrib import admin
from .models import Center, CenterImage, CenterReview
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

class CenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'site']
    search_fields = ['name', 'address']

class CenterReviewAdmin(admin.ModelAdmin):
    list_display = ['center', 'author', 'text', 'created_date']
    search_fields = ['center', 'author']
    list_filter = (
        ('created_date', DateTimeRangeFilter),
    )

admin.site.register(Center, CenterAdmin)
admin.site.register(CenterImage)
admin.site.register(CenterReview, CenterReviewAdmin)
