from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request):
  print "*"*10,' RANDOM WORD GENERATOR (def index)'
  if 'trials' not in request.session:
    request.session['trials']=0
  if request.method=='POST':
    # print request.POST
    if request.POST['loc']=='farm':
      return redirect('/farm')
    elif request.POST['loc']=='cove':
      return redirect('/cove') 
    elif request.POST['loc']=='house':
      return redirect('/house') 
    else:
      return redirect('/casino') 
  return render(request, "random_word/index.html")

