from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from time import gettime, strftime
# from django.utils.crypte import get_random_string

from models import *

def index(request):
  print '\n***** in TIME_DISPLAY INDEX\n'
  context = {
    'time': datetime.datetime.now()
  }
  return render(request, "time_display/index.html", context)

