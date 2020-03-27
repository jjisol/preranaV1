from django import forms
from .models import OnedayClassReview

class OnedayClassReviewForm(forms.ModelForm):

    class Meta:
        model = OnedayClassReview
        fields = ('text', )
