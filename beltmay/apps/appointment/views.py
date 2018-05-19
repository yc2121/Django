from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request):
  return render(request,'/index.html')

def register (request):

  print '\n',"*"*10,' def register\n'
  errors = User.objects.basic_validator(request.POST,'register')
  print errors

  if len(errors):
      for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
      return redirect('/')
  else:
    u=User.objects.create(
      name = request.POST['name'],
      alias = request.POST['alias'],
      email = request.POST['email'],
      password = bcrypt.hashpw( request.POST['password'].encode(), bcrypt.gensalt() )
      )
    u=User.objects.get(email=request.POST['email'])
    context = u
    
  context ={ 'where':'def register'}

  return render(request,'/body.html',context)

def login(request):  
  print '\n',"*"*10,' def login\n'

  errors = User.objects.basic_validator(request.POST,'login')

  if len(errors):
    for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
    return redirect('/')
  else:
    context={ 'name':request.POST['email'] }
    return render(request, '/body.html', context)

def books(request):
  print '\n',"*"*10,' def books\n'
  return redirect('/books.html')

def add_book_and_review(request):
  print '\n',"*"*10,' def add_book_and_review\n'
  return redirect('/book_and_review_form.html')

def review_details(request):
  print '\n',"*"*10,' def review_details\n'
  return redirect('/reviews_detail.html')

def user_review(request):
  print '\n',"*"*10,' def user_review\n'
  return redirect('/user_review.html')

def users(request):
  print '\n',"*"*10,' def users\n'
  
  if 'activities' not in request.session:
    request.session['activities']=[]

  if request.method=='POST':
    # print request.POST
    if request.POST['submit']=='register':
      return redirect('/register')
    else:
      return redirect('/bookreview')

def users_details(request, userid):
  print '\n',"*"*10,' def users_details\n'
  print 'userid=',userid
  context = {
    'user' : User.objects.get(id=userid)
  }
  print '\n CONTEXT \n',context

  return render(request, "/details.html", context)

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
