from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from django.utils.crypte import get_random_string

from models import *
from time import gmtime, strftime

def index(request):
  context = {
    "date": strftime("%M-%D-%d %H:%M %p", gmtime()),
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'time_display/index.html', context)

