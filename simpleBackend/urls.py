"""simpleBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from simpleDjangoApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^simple.html$', views.simpleDjangoApp_index),
    url(r'^login.html$', views.simpleDjangoApp_login),
    url(r'^exchange.html$', views.simpleDjangoApp_exchange),
    url(r'^classes.html$', views.simpleDjangoApp_showClasses, name="classes_url"),
    url(r'^editAClass$', views.simpleDjangoApp_editAClass),
    url(r'^delAClass$', views.simpleDjangoApp_delAClass),
    url(r'^addAClass$', views.simpleDjangoApp_addAClass),
    url(r'^students.html$', views.simpleDjangoApp_showStudents, name="students_url"),
    url(r'^addAStudent$', views.simpleDjangoApp_addAStudent),
    url(r'^teachers.html', views.simpleDjangoApp_showTeachers, name="teachers_url"),

]
