from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignInForm(forms.Form):

    username = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={'autofocus': '', 'class': 'form-control', 'placeholder': "账号或邮箱", 'id': "InputAccount",})
    )
    password = forms.CharField(max_length=20, min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "密码", 'id': "InputPassword"})
    )
    checkbox = forms.CheckboxInput()


class SignUpForm(forms.Form):

    username = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={'autofocus': '', 'class': 'form-control', 'placeholder': "账号", 'id': "SignUpAccount",})
    )
    password = forms.CharField(max_length=20, min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "密码", 'id': "SignUpPassword"})
    )
    repeat_password = forms.CharField(max_length=20, min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "重复密码", 'id': "RepeatPassword"})
    )

    # class Meta:
    #     model = User
    #     fields = ('username')
