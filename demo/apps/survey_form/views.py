from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request): 
  print '\n',"*"*10,' def index\n'
  return render(request,'survey_form/index.html')

def result(request):
  
  context = {
    'yourname':request.POST['yourname'],
    'location':request.POST['location'],
    'language':request.POST['language'],
    'comment':request.POST['comment'],
  }

  return render(request,'survey_form/result.html', context)

def runthis (request):

  return redirect('/')

def logout(request):
  print '\n',"*"*10,' def logout\n'
  request.session.flush()
  return redirect('/')

