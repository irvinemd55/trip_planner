# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt, re
from django.db import models
from datetime import datetime
from django.contrib import messages

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, postInfo):
        errors=[]
        if len(postInfo['name']) < 3:
            errors.append("Name must be greater than 3 characters.")       
        if len(postInfo['password']) < 8:
            errors.append("Password must be at least 8 characters long")
        if postInfo['password'] != postInfo['conf_password']:
            errors.append("Passords do no match")
        elif len(postInfo['username']) < 3:
            errors.append("Username must be greater than 3 characters.")
        if not errors:
            hashword = bcrypt.hashpw((postInfo['password'].encode()), bcrypt.gensalt())

            new_user = self.create(
                name=postInfo['name'],
                username=postInfo['username'],
                password=hashword,
                created_at = models.DateTimeField(auto_now_add=True),                
            )
            return new_user
        return errors

    def login(self, postInfo):
        errors = []

        if len(self.filter(username=postInfo['username'])) > 0:
            user = self.filter(username=postInfo['username'])[0]
            if not bcrypt.checkpw(postInfo['password'].encode(), user.password.encode()):
                errors.append('username/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return errors
        return user

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __str__(self):
        return self.username