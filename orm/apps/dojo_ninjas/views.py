from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request):
  print "*"*10,' DOJO NINJAS (def index)....'
  context = {
    "dojos": Dojo.objects.all(),
    "ninjas": Ninja.objects.all()
    }
  return render(request, "books/index.html", context)

