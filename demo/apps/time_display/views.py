from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from django.utils.crypte import get_random_string

from models import *
from time import gmtime, strftime

def index(request):
  print '\n******* IN INDEX'
  context = {
    'date': strftime('%b %d, %Y'),
    'time': strftime('%I:%M:%S %p')
  }
  return render(request,'time_display/index.html', context)

