from django import forms
from .models import Profile


class SignInForm(forms.Form):

    Account = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={'autofocus': '', 'class': 'form-control', 'placeholder': "账号或邮箱", 'id': "InputAccount",})
    )
    password = forms.CharField(max_length=20, min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "密码", 'id': "InputPassword"})
    )
    checkbox = forms.CheckboxInput()


# class SignUpForm(forms.Form):

