from django.shortcuts import render
from django.shortcuts import redirect
from .forms import AppointmentForm
from django.http import HttpResponse
import pdb
from appointments.models import Appointment
import json
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages

def index(request):
    form = AppointmentForm()
    return render(request,"appointments/index.html", {'form': form})

def create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment Created")
            return redirect("/")
        else:
            form = AppointmentForm()
            messages.error(request, "Error, Please try again")
            return render(request, "appointments/index.html", {'form': form})

def search(request):
    params = request.GET['params']
    if params:
        appointments = Appointment.objects.filter(description=params)
    else:
        appointments = Appointment.objects.all()
    appointments = appointments.values('datetime', 'description')
    response = JsonResponse(dict(appointments=list(appointments)))
    return response
