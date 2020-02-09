from django.contrib import admin
from .models import Center, CenterImage
from .forms import CenterForm

class CenterAdmin(admin.ModelAdmin):
    form = CenterForm
    list_display = ['name', 'phone', 'address', 'site']
    search_fields = ['name', 'address']

admin.site.register(Center, CenterAdmin)
admin.site.register(CenterImage)
