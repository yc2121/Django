from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

test = {
  'user' : 'Bruce Wayne',
  'email': 'bruce@batman.com',
  'pwd': 'so cool!',
  'other' : 'Ed, did you happen to see my mask?'
}

def index(request): 
  print '\n',"*"*10,' def index\n' 
  return render(request,'website/index.html', test)

def register(request):
  print '\n',"*"*10,' def register\n'
  print request.POST

  errors = User.objects.basic_validator(request.POST, 'register')
  print '***** In register and just returned from basic validator, \nerrors =',errors
  if errors:
    for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
    return redirect('/')
  else:
    u=User.objects.create(
      name = request.POST['name'],
      email = request.POST['email'],
      password = bcrypt.hashpw( request.POST['password'].encode(), bcrypt.gensalt() ),
      theDate = request.POST['theDate'],
      theTime = request.POST['theTime'],
      )

    request.session['userID']=u.id
    print request.session['userID'], User.objects.get(email=request.POST['email']).id

    return redirect('/user/{}/'.format(u.id))

def info(request, userID):
  print '\n',"*"*10,' def info for userID={}'.format(userID),'\n' 
  u=User.objects.get(id=int(userID))
  info = {
    'userID': u.id,
    'name' : u.name,
    'email' : u.email,
    'theDate' : u.theDate,
    'theTime' : u.theTime,
    }

  theRest=[]
  for each in User.objects.exclude(id=u.id)[:3]:
    theRest += [{
      'userID': each.id,
      'name' : each.name,
      'email' : each.email,
      'theDate' : each.theDate,
      'theTime' : each.theTime,
      }]

  context = {
    'info': info,
    'theRest': theRest
  }

  return render(request,'website/infopage.html', context)

def thisPage(request, thisID):
  if request.method=='post':
    redirect ('/user/{}/edit'.format(thisID))
  else:

    u = User.objects.get(id=thisID)
    context = {
      'user': u
    }
    return render(request,'website/thisPage.html', context)

def edit(request,userID):

  return redirect('/')


def login(request):
  print '\n',"*"*10,' def login\n'
  
  errors = User.objects.basic_validator(request.POST, 'login')
  print '***** In login and just returned from basic validator, \nerrors =',errors
  if errors:
    for tag, error in errors.iteritems():
      messages.error(request, error, extra_tags=tag)
    return redirect('/')
  else:
    request.session['userID']=User.objects.get(email=request.POST['email']).id
    
    return redirect('/user/{}/'.format(request.session['userID']))

def logout(request):
  print '\n',"*"*10,' def logout\n'
  request.session.flush()
  return redirect('/')
