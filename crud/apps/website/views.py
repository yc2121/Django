from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

testData = {
  'user' : 'Bruce Wayne',
  'email': 'bruce@batman.com',
  'pwd': 'so cool!',
  'theDate': '2018-04-01',
  'theTime': '13:30',
  'other' : 'Ed, did you happen to see my mask?',
  'pwdMin': 3,
}

def index(request): 
  print '\n',"*"*10,' def index\n'
  return render(request,'website/index.html', testData)

def register(request):
  print '\n',"*"*10,' def register\n'

  errors = User.objects.basic_validator(request.POST, 'register')
  print '***** Validation errors =',errors
  if errors:
    for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
    if request.session['addUser']:
      return redirect('/user/add/')
    else:
      return redirect('/')
  else:
    try:
      u=User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        password = bcrypt.hashpw( request.POST['password'].encode(), bcrypt.gensalt() ),
        admin = False,
        theDate = request.POST['theDate'],
        theTime = request.POST['theTime'],
        )
      request.session['userID']=u.id
      print 'Session established for {}'.format(u)        
      return redirect('/user/{}/'.format(request.session['userID']))
    except:
      print '------> Error in creating user object for \n{}'.format(u)

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
  print '***** Validation errors =',errors

  if errors:
    for tag, error in errors.iteritems():
      messages.error(request, error, extra_tags=tag)
    return redirect('/')
  else:
    request.session['userID']=User.objects.get(email=request.POST['email']).id
    print 'Session established for user [{}]'.format(request.session['userID'])
    return redirect('/user/{}/'.format(request.session['userID']))

def logout(request):
  print '\n',"*"*10,' def logout\n'
  request.session.flush()
  return redirect('/')

def info(request, userID):
  print '\n',"*"*10,' def info for userID={}'.format(userID),'\n'
  request.session['thisUser']=userID
  try:  
    u=User.objects.get(id=request.session['thisUser'])

    thisUser = {
      'id': u.id,
      'name' : u.name,
      'email' : u.email,
      'admin' : u.admin,
      'theDate' : u.theDate,
      'theTime' : u.theTime,
      }
  except:
    print '------> Error in getting in user object: \n{}'.format(u)

  try:
    theRestUsers=[]
    if u.admin:
      for each in User.objects.exclude(id=request.session['thisUser'])[:3]:
        theRestUsers += [{
          'id': each.id,
          'name' : each.name,
          'email' : each.email,
          'admin' : each.admin,
          'theDate' : each.theDate,
          'theTime' : each.theTime,
          }]
  except:
    print '------> Error in getting the rest users: \n{}'.format(u)
  
  context = {
    'thisUser': thisUser,
    'theRestUsers': theRestUsers
  }

  return render(request,'website/infopage.html',context)

def addUser(request):
  request.session['addUser']=True
  return render(request,'website/addUser.html', testData)
