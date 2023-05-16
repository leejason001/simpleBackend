# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
import models
import json

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
    classesData = models.myClass.objects.all()
    for data in classesData:
        data.caption = data.caption.encode("utf-8")
        print data.caption
        print type(data.caption)
        print type(data.id)

    return render(request, "classes.html", {"classesData":classesData})

def simpleDjangoApp_editAClass(request):
    pass

def simpleDjangoApp_delAClass(request):
    models.myClass.objects.get(id=request.POST.get("delingClass_id")).delete()
    return HttpResponse(2222)

def simpleDjangoApp_addAClass(request):
    newClass = models.myClass.objects.create(
        caption=request.POST.get("newClassCaption")
    )

    return HttpResponse(json.dumps({"newClass_id":newClass.id, "newClass_caption":newClass.caption}))
