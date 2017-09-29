# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def authenticate(request):
    result = User.objects.login(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect(reverse("main:index"))
    request.session['user_id'] = result.id
    return redirect(reverse("travels:travels"))

def register_user(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:   
        for error in result:
            messages.error(request, error)
        return redirect(reverse("main:index"))
    request.session['user_id'] = result.id
    return redirect(reverse("travels:travels"))

def logout(request):
    request.session.clear()
    return redirect(reverse("main:index"))