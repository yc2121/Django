from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request):
  print '\n',"*"*10,' BOOKS (def index)\n'

  for author in Author.objects.all():
    for theid in author.id:
      print Book.objects.get(id=str(theid)).authors   
      context = { 
        "authors": theid,
        "books": 'test'
        }

  # context={}
  # print '\n', context
  return render(request, "books/index.html", context)

  # if 'yourgold' not in request.session:
  #   request.session['yourgold']=0
  # if 'activities' not in request.session:
  #   request.session['activities']=[]
  # if request.method=='POST':
  #   # print request.POST
  #   if request.POST['loc']=='farm':
  #     return redirect('/farm')
  #   elif request.POST['loc']=='cove':
  #     return redirect('/cove') 
  #   elif request.POST['loc']=='house':
  #     return redirect('/house') 
  #   else:
  #     return redirect('/casino') 



