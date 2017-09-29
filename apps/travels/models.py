# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..main.models import User
from datetime import date

# Create your models here.

class TripManager(models.Manager):
    
    def check(self, postInfo):
        errors=[]
        if len(postInfo['description']) < 1 or len(postInfo['destination']) < 1:
            errors.append("No empty fields.")
        elif len(postInfo['start_date']) < 1 or len(postInfo['end_dat']) < 1:
            errors.append('No empty fields.')
        if not errors:
            new_trip = self.create(
                destination = postInfo['destination'],
                description = postInfo['description'],
                start_date = postInfo['start_date'],
                end_date = postInfo['end_date'],
                planner = User.objects.get(id=request.session['user_id'])
            )
            return new_trip
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    planner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="planner")
    participants = models.ManyToManyField(User)