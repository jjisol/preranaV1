from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ('title', 'text',)

        widgets={
            "title":forms.Textarea(attrs={'class':'form-control','rows':1}),
            "text":forms.Textarea(attrs={'placeholder':'공지를 작성해주세요.','class':'form-control','rows':5}),
        }
