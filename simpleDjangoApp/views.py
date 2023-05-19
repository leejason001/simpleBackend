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

    return render(request, "classes.html", {"classesData":classesData})

def simpleDjangoApp_editAClass(request):
    theClassModelObject = models.myClass.objects.get(id=request.POST.get("editClass_id"))
    print theClassModelObject.caption
    print request.POST.get("editClass_caption")
    theClassModelObject.caption = request.POST.get("editClass_caption")
    theClassModelObject.save()
    return HttpResponse(theClassModelObject.caption)

def simpleDjangoApp_delAClass(request):
    models.myClass.objects.get(id=request.POST.get("delingClass_id")).delete()
    return HttpResponse(2222)

def simpleDjangoApp_addAClass(request):
    newClass = models.myClass.objects.create(
        caption=request.POST.get("newClassCaption")
    )

    return HttpResponse(json.dumps({"newClass_id":newClass.id, "newClass_caption":newClass.caption}))

def simpleDjangoApp_showStudents(request):
    if "GET" == request.method:
        classes = models.myClass.objects.all()
        studentsInfo = models.myStudent.objects.all()
        return render(request, "students.html", {"classes":classes, "studentsInfo":studentsInfo})

def simpleDjangoApp_addAStudent(request):
    # print request.POST.get("turename")
    aNewStudent = models.myStudent.objects.create(
        name = request.POST.get("truename"),
        cls = models.myClass.objects.get(id=int(request.POST.get("ownClass_id"))),
        username = request.POST.get("username"),
        password = request.POST.get("password"),
    )
    classes = models.myClass.objects.all()
    studentsInfo = models.myStudent.objects.all()
    return render(request, "students.html", {"classes": classes, "studentsInfo": studentsInfo})

def simpleDjangoApp_showTeachers(request):
    teachers = models.myTeacher.objects.all()
    return render(request, "teachers.html", {"teachers": teachers})
