from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request):
  print '\n',"*"*10,' SAMPLE (def index)\n'
  # if 'activities' not in request.session:
  #   request.session['activities']=[]
  if request.method=='POST':
    if request.POST['click']=='register':
      return redirect('/register')
    else:
      request.POST['click']=='login'
      return redirect('/login') 
  else:
    return render(request,'sample/index.html')

def register (request):
  print '\n',"*"*10,' SAMPLE (def register)\n'
  print 'Request.POST["email_addr"]=',request.POST['email_addr']
  errors = User.objects.basic_validator(request.POST,'registeration')
  if len(errors):
      for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
      return redirect('/')
  else:
      User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email_addr'],
        password = request.POST['pwd']
        )
      blog.save()
      return redirect('/')
  context ={
    'x':'123',
    'y':'456'
  }

  return render(request,'sample/reg-login-result.html',context)

def login(request):
  print '\n',"*"*10,' SAMPLE (def login)\n'

  context ={
    'x':'123',
    'y':'456'
  }

  return render(request,'sample/reg-login-result.html',context)

def users(request):
  print '\n',"*"*10,' SAMPLE (def users)\n'
  
  if 'activities' not in request.session:
    request.session['activities']=[]

  if request.method=='POST':
    # print request.POST
    if request.POST['submit']=='register':
      return redirect('/register')
    else:
      return redirect('/sample')

def users_details(request, userid):
  print '\n',"*"*10,' SAMPLE (def users_details)\n'
  print 'userid=',userid
  context = {
    'user' : User.objects.get(id=userid)
  }
  print '\n CONTEXT \n',context

  return render(request, "sample/details.html", context)

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



