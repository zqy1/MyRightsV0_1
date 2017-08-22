# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import View 基于类的视图
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Profile
from django.contrib.auth.models import User
from .forms import SignInForm


def welcome(request):
    return HttpResponse("<h1>hello臧奇颜</h1>")


def sign_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        username = request.POST.get('Account')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse('登陆错误')

    content = {
        'user': None,
    }
    return render(request, 'Account/sign_in.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def sign_up(request):

    return render(request, 'Account/sign_up.html')


def test(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    state = None
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username=cd['Account'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    state = 'disabled_account'
                    # 未实现
                    # return HttpResponse('disabled account')
            else:
                state = 'not_exist'
    else:
        form = SignInForm()

    content = {'form': form, 'state': state}
    return render(request, 'Account/test.html',content)
