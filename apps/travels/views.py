# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from ..main.models import User
from .models import Trip
from django.shortcuts import render, redirect, reverse


# Create your views here.
def travels(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'trips': Trip.objects.all(),
    }
    return render(request, 'travels/travels.html', context)

def show(request, trip_id):  
    print Trip.objects.get(id=trip_id).description
    context = {
        'trip': Trip.objects.get(id=trip_id),
    }
    return render(request, 'travels/show.html', context)

def add(request):
    return render(request, 'travels/add.html')


def new(request):
    
    # result = Trip.objects.check(request.POST)
    # if type(result) == list:
    #     for error in result:
    #         messages.error(request, error)
    #         return redirect(reverse("travels:new"))

    new_trip = Trip.objects.create(
        destination = request.POST['destination'],
        description = request.POST['description'],
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        planner = User.objects.get(id=request.session['user_id']),
        )
    
    new_trip.participants.add(User.objects.get(id=request.session['user_id']))

    return redirect(reverse("travels:travels"))

def join(request, trip_id):
    new_trip = Trip.objects.get(id=trip_id)
    new_trip.participants.add(User.objects.get(id=request.session['user_id']))
    return redirect(reverse("travels:travels"))

def logout(request):
    request.session.clear()
    return redirect(reverse("main:index"))