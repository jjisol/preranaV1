from django import forms
from .models import Center

class CenterForm(forms.ModelForm):

    class Meta:
        model = Center
        fields = ['name', 'type', 'detail', 'price', 'info', 'event', 'schedule',
            'phone', 'address', 'site',]
        widgets = {
            'type':forms.CheckboxSelectMultiple,
        }
