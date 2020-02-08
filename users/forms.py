from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    passwordCheck = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'password2',
        'id': 'password2',
        'placeholder': 'Password',}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'passwordCheck', 'email')

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'name': 'email',
                    'id': 'email',
                    'type': 'text',
                }),

            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'name': 'name',
                    'id': 'name',
                    'type': 'text',
                }),

            'password': forms.PasswordInput(
                attrs={
                    'class': 'password',
                    'name': 'password',
                    'placeholder': 'Password',
                }),

            'passwordCheck': forms.PasswordInput(
                attrs={
                    'class': 'password2',
                    'id': 'password2',
                    'placeholder': 'Password',
                }),
            }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15
#    def save(self, commit=True):
#        user = super().save(commit=False)
#        user.set_password(self.cleaned_data["password"])
#        if commit:
#            user.save()
#        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'input100',
                    'type': 'text',
                    'name': 'username',
                }),

            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'class': 'input100',
                    'type': 'password',
                    'name': 'password',
                }),
        }

class DeleteAccountForm(forms.Form):
    password = forms.CharField()

class FindUsernameForm(forms.Form):
    email = forms.CharField()

class FindPasswordForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name','last_name']
