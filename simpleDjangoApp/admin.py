# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import myClass,myStudent,myTeacher

admin.site.register(myClass)
admin.site.register(myStudent)
admin.site.register(myTeacher)