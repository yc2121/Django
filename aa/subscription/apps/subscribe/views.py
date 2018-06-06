from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request): 
  print '\n',"*"*10,' def index\n' 
  return render(request,'subscribe/index.html')

def register(request):

  print '\n',"*"*10,' def register\n'
  
  errors = User.objects.basic_validator(request.POST,'register')
  print '***** errors =',errors
  
  if errors:
      for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
      return redirect('/')
  else:
    u=User.objects.create(
      name = request.POST['name'],
      email = request.POST['email'],
      password = bcrypt.hashpw( request.POST['password'].encode(), bcrypt.gensalt() ),
      # dob = request.POST['dob'],
      )
    request.session['userID']=User.objects.get(email=request.POST['email']).id
    context = u
  print '***** context =',u
  return redirect('/user/{}/'.format(request.session['userID']))

def login(request):
  
  print '\n',"*"*10,' def login\n'

  errors={}
  # Email format
  if not email_regex.match(request.POST['email']):
    errors['email']='"{}" is not a valid email address.'.format(request.POST['email'])
    for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
    return redirect('/')
  else:
    if User.objects.filter(email=request.POST['email']).exists():
      u=User.objects.get(email=request.POST['email'])
      print 'Checking password for {}'.format(u.name)
      if bcrypt.checkpw( request.POST['password'].encode(), u.password.encode()):
        print 'Passowrd matched for {}'.format(u.name)
        request.session['userID']=u.id
        if u.admin:
          return redirect ('/package/') 
        else:
          return redirect ('/user/{}/'.format(u.id))
      else:
        print "Incorrect password"
        errors['password'] = 'Incorrect password!'
        for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
      print '"{}" is not a registered user.'.format(request.POST['email'])
      errors['email'] = '"{}" is not a registered user.'.format(request.POST['email'])
      for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
      return redirect('/')

def logout(request):
  
  print '\n',"*"*10,' def logout\n'
  del request.session
  return redirect('/')

def userpage(request, userid):

  print '\n',"*"*10,' def userpage\n'
  u=User.objects.get(id=userid)
  p=Package.objects.filter(users__id=userid)
  count=0; total=0
  for i in p:
    if i.available == True:
      # print '{},{},{},{}'.format(i.id, i.name, i.cost, i.available)
      total+=i.cost
      count+=1
  
  anns=Package.objects.filter(available=True).exclude(users__id=userid)
  print '===> anns', anns

  context = {
    'name':u.name,
    'packages':p,
    'monthly': total//12,
    'count': count,
    'anns':anns #available_n_nonsubscribed
  }
  return render(request,'subscribe/userpage.html',context)

def add(request, packageID):

  print '\n',"*"*10,' def add\n'
  
  u=User.objects.get(id=request.session['userID'])
  u.packages.add(packageID)
  p=u.packages.all()

  count=0; total=0
  for i in p:
    if i.available == True:
      # print '{},{},{},{}'.format(i.id, i.name, i.cost, i.available)
      total+=i.cost
      count+=1
  
  anns=Package.objects.filter(available=True).exclude(
    users=request.session['userID']
    )
  print '===> anns', anns

  context = {
    'name':u.name,
    'packages':p,
    'monthly': total//12,
    'count': count,
    'anns':anns #available_n_nonsubscribed
  }
  return render(request,'subscribe/userpage.html',context)

def delete(request, packageID):
  
  print '\n',"*"*10,' def delete\n'
  
  u=User.objects.get(id=request.session['userID'])
  
  ## HOW TO DELETE A FOREIGN KEY, THE FOLLOWING WILL DELETE THE RECORD
  u.packages.get(id=packageID).delete()

  p=u.packages.all()
  count=0; total=0
  for i in p:
    if i.available == True:
      # print '{},{},{},{}'.format(i.id, i.name, i.cost, i.available)
      total+=i.cost
      count+=1
  
  anns=Package.objects.filter(available=True).exclude(
    users=request.session['userID']
    )
  print '===> anns', anns

  context = {
    'name':u.name,
    'packages':p,
    'monthly': total//12,
    'count': count,
    'anns':anns #available_n_nonsubscribed
  }
  return render(request,'subscribe/userpage.html',context)

def package(request):

  print '\n',"*"*10,' def package\n'

  u=User.objects.first()
  p=u.packages.all()

  count=0; total=0
  for i in p:
    if i.available == True:
      # print '{},{},{},{}'.format(i.id, i.name, i.cost, i.available)
      total+=i.cost
      count+=1
  
  allp=Package.objects.all()
  for p in allp:
    Package.objects.users.count()

  context = {
    'name':u.name,
    'packages':p,
    'monthly': total//12,
    'count': count,
    'allp':allp #all packages
  }
  return render(request,'subscribe/adminpage.html',context)

