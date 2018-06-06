from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime
username_regex = re.compile(r'^[a-zA-Z0-9]{3,}$')

def index(request): 
  print '\n',"*"*10,' def index\n' 
  return render(request,'website/index.html')

def register(request):
  print '\n',"*"*10,' def register\n'

  errors = User.objects.basic_validator(request.POST)
  print '***** In register and just returned from basic validator, \nerrors =',errors
  
  if errors:
      for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
      return redirect('/')
  else:

    u=User.objects.create(
      name = request.POST['name'],
      username = request.POST['username'],
      password = bcrypt.hashpw( request.POST['password'].encode(), bcrypt.gensalt() ),
      doh = request.POST['doh'],
      )
    request.session['userID']=User.objects.get(username=request.POST['username']).id

    print '***** leaving regiter, context =',u
    return redirect('/dashboard/')
  # return redirect('/user/{}/'.format(request.session['userID']))

def login(request):
  print '\n',"*"*10,' def login\n'

  errors={}
  # Email format
  if not username_regex.match(request.POST['username']):
    errors['username']='"{}" must be with 3 or more\
      of the acceptable characters: A-Za-z0-9.'.format(request.POST['username'])
    for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
    return redirect('/')
  else:
    if User.objects.filter(username=request.POST['username']).exists():
      u=User.objects.get(username=request.POST['username'])
      print 'Checking password for {}'.format(u.name)
      if bcrypt.checkpw( request.POST['password'].encode(), u.password.encode()):
        print 'Passowrd matched for {}'.format(u.name)
        request.session['userID']=u.id
        return redirect('/dashboard/')
      else:
        print "Incorrect password"
        errors['password'] = 'Incorrect password!'
        for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
      print '"{}" is not a registered user.'.format(request.POST['username'])
      errors['username'] = '"{}" is not a registered user.'.format(request.POST['username'])
      for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
      return redirect('/')

def logout(request):
  print '\n',"*"*10,' def logout\n'
  request.session.flush()
  return redirect('/')

def dashboard(request):

  print '\n',"*"*10,' def dashboard\n'
  
  u=User.objects.get(id=request.session['userID'])
  # user added items
  items=Item.objects.filter(users__id=u.id)
  print '===> items=',items
  
  more=Item.objects.exclude(users__id=u.id)
  print '===> items=',more

  context = {
    'name':u.name,
    'items':items,
    'more':more
  }
  return render(request,'website/dashboard.html',context)

def create(request):
  print '\n',"*"*10,' def create\n'
  return render(request,'website/newitem.html')

def newitem(request):

  errors = Item.objects.basic_validator(request.POST)
  
  if errors:
      for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
        return render(request,'website/newitem.html')
  else:
    # add an item with the relationship
    u=User.objects.get(id=request.session['userID'])
    Item.objects.create(item=request.POST['item']).users.add(u.id)

    items=Item.objects.filter(users__id=u.id)
    more=Item.objects.all().exclude(users__id=u.id)
    print '===> items=',items
    context = {
      'name':u.name,
      'items':items,
      'more':more
    }
    return render(request,'website/dashboard.html',context)

def add(request, itemName):

  print '\n',"*"*10,' def add\n'

  u=User.objects.get(id=request.session['userID'])
  u.items.create(item=itemName)
  
  items=Item.objects.filter(users__id=u.id)
  more=Item.objects.all().exclude(users__id=u.id)
  print '===> items=',items
  context = {
    'name':u.name,
    'items':items,
    'more':more
  }
  return render(request,'website/dashboard.html',context)

def view(request, itemid):

  thisItem=Item.objects.get(id=itemid)
  # u=thisItem.users.all()
  # create_by=thisItem.users.all()

  context ={
    'thisItem':thisItem,
    # 'created_by': u.id
  }

  return render(request,'website/item.html',context)

def delete(request, itemid):
  
  print '\n',"*"*10,' def delete\n'
  
  u=User.objects.get(id=request.session['userID'])
  
  # remove the many-to-many key
  u.items.remove(itemid)

  # Delete an item
  # Item.objects.get(id=80).delete()

  # update and redisplay the list
  items=Item.objects.filter(users__id=u.id)
  more=Item.objects.all().exclude(users__id=u.id)

  context = {
    'name':u.name,
    'items':items,
    'more':more
  }
  return render(request,'website/dashboard.html',context)

