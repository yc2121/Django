from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from forms import LoginForm

from models import *
import os, random, datetime, bcrypt

def index(request):
  # print '\n',"*"*10,' CRUD (def index)\n'
  # if request.method=='POST':
  #   if request.POST['click']=='register':
  #     return redirect('/register')
  #   else:
  #     request.POST['click']=='login'
  #     return redirect('/login') 
  # else:
  #   return render(request,'crud/index.html')
  # return render(request,'crud/index.html')
  return render(request,'crud/index.html')

def register (request):

  print '\n',"*"*10,' CRUD (def register)\n'
  errors = User.objects.basic_validator(request.POST,'register')
  print errors

  if len(errors):
      for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
      return redirect('/')
  else:
    u=User.objects.create(
      first_name = request.POST['first_name'],
      last_name = request.POST['last_name'],
      email = request.POST['email'],
      password = bcrypt.hashpw( request.POST['password'].encode(), bcrypt.gensalt() )
      )
    u=User.objects.get(email=request.POST['email'])
    context = u
    return render(request,'crud/body.html',context)

def login(request):
  
  print '\n',"*"*10,' CRUD (def login)\n'

  errors = User.objects.basic_validator(request.POST,'login')

  if len(errors):
      for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
      return redirect('/')
  else:
      u = User.objects.get(email = request.POST['email'])
      context = {
        'first_name':u.first_name,
        'last_name':u.last_name,
        'email':u.email,
      }
  return render(request, 'crud/body.html', context)

def users(request):
  print '\n',"*"*10,' CRUD (def users)\n'
  
  if 'activities' not in request.session:
    request.session['activities']=[]

  if request.method=='POST':
    # print request.POST
    if request.POST['submit']=='register':
      return redirect('/register')
    else:
      return redirect('/crud')

def users_details(request, userid):
  print '\n',"*"*10,' CRUD (def users_details)\n'
  print 'userid=',userid
  context = {
    'user' : User.objects.get(id=userid)
  }
  print '\n CONTEXT \n',context

  return render(request, "crud/details.html", context)

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



