# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..logreg_app.models import User
from django.db import models
import datetime

class ApptManager(models.Manager):
    def appt_validation(self,data):
        now = Appt(date=datetime.date.today())
        errors = {}
        # if str(data['date']) < now:
        #     errors["date"] = "Date field cannot be previous to current date"
        if len(data['date']) < 1:
            errors["date"] = "Date field must be entered"

        if len(data['time']) < 1:
            errors["time"] = "Time field must be entered"

        if len(data['task']) < 1:
            errors["task"] = "Task field must be entered"
    
        # if int(data['date']) < now:
        #     errors["date"] = "Date cannot be previous to current date"
        return errors

    # def addfavorites(self, userid, quoteid):
    #     f1 = User.objects.get(id = userid)
    #     f2 = New.objects.get(id = quoteid)
    #     f2.favorites.add(f1)
    #     f2.save()

    # def removefavorites(self, userid, quoteid):
    #     f1 = User.objects.get(id = userid)
    #     f2 = New.objects.get(id = quoteid)
    #     f2.favorites.remove(f1)
    #     f2.save()

class Appt(models.Model):
    user = models.ForeignKey(User, related_name='users')
    status = models.CharField(max_length = 255)
    tasks = models.TextField(max_length = 1000)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    objects = ApptManager()
# Create your models here.
