from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request):
  print '\n',"*"*10,' LOGIN (def index)\n'

  context={

  }

  return render(request, "login/index.html", context)

def register (request):
  print '\n',"*"*10,' LOGIN (def register)\n'
  errors = User.objects.basic_validator(request.POST)
  if len(errors):
      for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
      return redirect('/')
  else:
      blog = User.objects.get(id = id)
      blog.name = request.POST['full_name']
      blog.name = request.POST['email']
      blog.save()
      return redirect('/')

def users(request):
  print '\n',"*"*10,' LOGIN (def users)\n'
  
  if 'activities' not in request.session:
    request.session['activities']=[]

  if request.method=='POST':
    # print request.POST
    if request.POST['submit']=='register':
      return redirect('/register')
    else:
      return redirect('/login')

def login(request):
  print '\n',"*"*10,' LOGIN (def login)\n'

  return redirect('/')

def users_details(request, userid):
  print '\n',"*"*10,' LOGIN (def users_details)\n'
  print 'useridD=',userid
  context = {
    'user' : User.objects.get(id=userid)
  }
  print '\n CONTEXT \n',context

  return render(request, "login/details.html", context)

# def update(request):
#     errors = Blog.objects.basic_validator(request.POST)
#         if len(errors):
#             for tag, error in errors.iteritems():
#                 messages.error(request, error, extra_tags=tag)
#             return redirect('/blog/edit/'+id)
#         else:
#             blog = Blog.objects.get(id = id)
#             blog.name = request.POST['name']
#             blog.desc = request.POST['desc']
#             blog.save()
#             return redirect('/blogs')

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



