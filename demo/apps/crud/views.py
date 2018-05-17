from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request):
  print '\n',"*"*10,' CRUD (def index)\n'

  context={

  }

  return render(request, "crud/index.html", context)

def users(request):
  print '\n',"*"*10,' CRUD (def users)\n'

  context = {
    'users' : User.objects.all()
  }
  print '\n CONTEXT \n',context

  return render(request, "crud/users.html", context)

def users_details(request, userid):
  print '\n',"*"*10,' CRUD (def users_details)\n'
  print 'useridD=',userid
  context = {
    'user' : User.objects.get(id=userid)
  }
  print '\n CONTEXT \n',context

  return render(request, "crud/details.html", context)

  # for author in Author.objects.all():
  #   context = {
  #     "authors": author,
  #     "books": Author.books.all(),   
  #   }
  # print '\n', context

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



