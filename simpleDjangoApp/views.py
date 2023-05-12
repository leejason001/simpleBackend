# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

# Create your views here.
def simpleDjangoApp_index(request):
    if request.COOKIES.get('username'):
        return redirect("/exchange.html")
    else:
        return render(request, "login.html")

def simpleDjangoApp_login(request):
    nextPage = redirect("exchange.html")
    nextPage.set_cookie("username", request.POST.get("username"))
    return nextPage

def simpleDjangoApp_exchange(request):
    return render(request, "exchange.html")

def simpleDjangoApp_showClasses(request):
    classesData = myClass.objects.all()
    print classesData
    return render(request, "classes.html")
