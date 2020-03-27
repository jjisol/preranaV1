from django import forms
from .models import CenterReview

class CenterReviewForm(forms.ModelForm):

    class Meta:
        model = CenterReview
        fields = ('text', )
