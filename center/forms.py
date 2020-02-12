from django import forms
from .models import Center

class CenterForm(forms.ModelForm):
    type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
            choices=Center.TYPE_CHOICES)
    class Meta:
        model = Center
        fields = ['name', 'type', 'detail', 'price', 'info', 'event', 'schedule',
            'phone', 'address', 'site',]
