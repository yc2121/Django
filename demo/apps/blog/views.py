from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from time import gettime, strftime
# from django.utils.crypte import get_random_string

from models import *

# def index(request):
#   response = "Hello, from INDEX!"
#   return HttpResponse(response)

def index(request):
  context = {
      "email" : "blog@gmail.com",
      "name" : "mike"
  }
  return render(request, "blog/index.html", context)

def new(request):
  response = "Hello, from NEW!"
  return HttpResponse(response)

def create(request):
  if request.method == "POST":
    print "*"*50
    print request.POST
    print request.POST['name']
    print request.POST['desc']
    request.session['name'] = "test"  # more on session below
    print "*"*50
    return redirect("/")
  else:
    return redirect("/")

def show(request,num):
  response = "PLACE HOLDER FOR BLOG "+num
  return HttpResponse(response)

def edit(request,num):
  response = "PLACE HOLDER FOR EDITING BLOG "+num
  return HttpResponse(response)

def destroy(request,num):
  print "\n***** PLACE HOLDER FOR DELETING BLOG "+num+"\n"
  return redirect('/')
