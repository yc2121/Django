from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from time import gettime, strftime
# from django.utils.crypte import get_random_string

from models import *
import os, random, datetime

# def index(request):
#   response = "Hello, from INDEX!"
#   return HttpResponse(response)

def index(request):
  print "*"*10,' Start digging....'
  if not 'yourgold' in request.session:
    request.session['yourgold']=0
    request.session['activities']=[]
  if request.method=='POST':
    print request.POST
    if request.POST['loc']=='farm':
      return redirect('/farm')
    elif request.POST['loc']=='cove':
      return redirect('/cove') 
    elif request.POST['loc']=='house':
      return redirect('/house') 
    else:
      return redirect('/casino') 
  return render(request, "ninja_gold/index.html")

def farm(request):
  x=random.randrange(10,21); request.session['yourgold']+=x
  request.session['activities']+='Earned '+str(x)+ \
    ' golds from the Cave! ('+str(datetime.datetime.now())+')'
  return redirect('/')

def cove(request):
  x=random.randrange(5,11); request.session['yourgold']+=x
  request.session['activities']+='Earned '+str(x)+ \
    ' golds from the Cave! ('+str(datetime.datetime.now())+')'
  return redirect('/')

def house(request):
  x=random.randrange(2,6); request.session['yourgold']+=x
  request.session['activities']+='Earned '+str(x)+ \
    ' golds from the Cave! ('+str(datetime.datetime.now())+')'
  return redirect('/')

def casino(request):
  x=random.randrange(-50,51); request.session['yourgold']+=x
  request.session['activities']+='Earned '+str(x)+ \
    ' golds from the Cave! ('+str(datetime.datetime.now())+')'
  return redirect('/')
