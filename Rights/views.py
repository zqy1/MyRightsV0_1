# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'user': user,
    }
    return render(request, 'Rights/index.html', content)

def hello(request):
    return HttpResponse('<h2>嘿嘿</h2>')