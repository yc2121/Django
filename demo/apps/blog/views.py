# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
  response = "Hello, from INDEX!"
  return HttpResponse(response)

def new(request):
  response = "Hello, from NEW!"
  return HttpResponse(response)

def create(request):
  response = "Hello, from CREATE!"
  return HttpResponse(response)

def show(request,num):
  response = "PLACE HOLDER FOR BLOG "+num
  return HttpResponse(response)

def edit(request,num):
  response = "PLACE HOLDER FOR EDITING BLOG "+num
  return HttpResponse(response)

def destroy(request,num):
  response = "PLACE HOLDER FOR DELETING BLOG "+num
  return redirect('http://localhost:8000')
