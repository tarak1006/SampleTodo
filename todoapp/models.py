# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todolists(models.Model):
    name = models.CharField(max_length=128)
    creation_date = models.DateField(null=True, blank=True)
    user=models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Todoitems(models.Model):
    description = models.CharField(max_length=128)
    completed = models.BooleanField()
    due_by=models.DateField(null=True,blank=True)
    todolist = models.ForeignKey(Todolists)

    def __unicode__(self):
        return self.description