from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, string

def index(request):
  print "*"*10,' RANDOM WORD GENERATOR (def index)'
  if 'trials' not in request.session:
    request.session['trials']=0
  return render(request, "random_word/index.html")    

def random_string(size, chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def word(request):
  context ={
    'word':random_string(14),
  }
  request.session['trials']+=1
  return render(request, "random_word/index.html",context)

