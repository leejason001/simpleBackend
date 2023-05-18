# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class myClass(models.Model):
    caption  = models.CharField(max_length=32)

    def __str__(self):
        return self.caption.encode("utf8")


class myStudent(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ForeignKey("myClass")

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class myTeacher(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ManyToManyField("myClass")

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)