# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.db import models
import re, bcrypt

# # email_regex=r'[^@]+@[^@]+\.[^@]'
# name_min = 2; pwmin=8
name_regex = re.compile(r'^[ a-zA-Z0-9.+_-]{5,10}$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pwd_regex = re.compile(r'^[ !A-Za-z0-9@#$%^&=+_-]{8,}$')

class UserManager(models.Manager):

  def basic_validator(self, postData, type):
      
    errors = {}
    print '\n',"*"*10,' def basic-validator)\n'

    # Already registered
    if User.objects.filter(email=postData['email']).exists():
      errors['email'] = '"{}" has already registered.'.format(postData['email'])

    # Email format
    if not email_regex.match(postData['email']):
      errors['email']='"{}" is not a valid email address.'.format(postData['email'])
                
    # Name format
    if not name_regex.match(postData['name']):
      errors['name']='"{}" is not in a valid name format.'.format(postData['name'])
        
    # Password confirmation
    if postData['password'] != postData['confirmation']:
      errors['password']='Password and confirmed password do not match.'
    
    # Password complexities
    if not pwd_regex.match(postData['password']):
      errors['password']='Password string must be with 8 or more\
       of the acceptable characters: !A-Za-z0-9@#$%^&=+_-"'
      
    print 'Errors = {}'.format(errors)

    return errors
      
class User(models.Model):
  name = models.CharField(max_length=30)
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=30)
  admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  objects = UserManager()
  
  def __repr__(self):
		return '\n user [{}] - {}, {}, {}'.\
      format(self.id,self.name,self.email,self.admin)

# QUERIES:
# 1. all non-admin user
# User.objects.filter(admin=False)
# 2. all paackages for a user
# User.objects.get(id=1).packages.all()

# User.objects.create(name='johhn', email='j@abc.com', password='secret',admin=False)
# User.objects.filter(admin=False)
# User.objects.get(id=1).packages.add(2)
# User.objects.get(id=1).packages.all()

class PackageManager(models.Manager):

  def basic_validator(self, postData, type):
      
    errors = {}
    print '\n',"*"*10,' def basic-validator)\n'

    if not name_regex.match(postData['name']):
      errors['pkgname']='Package name must be with no space and\
       with 5 to 10 of the acceptable characters: !A-Za-z0-9@#$%^&=+_-"'

    if postData['cost']<0:
      errors['pkgcost']='Package prince must be a positive value.'
      
    print 'Errors = {}'.format(errors)

    return errors

class Package(models.Model):
  name = models.CharField(max_length=30)
  cost = models.FloatField(default=0.0)
  available = models.BooleanField(default=True)
  users = models.ManyToManyField(User, related_name='packages')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = PackageManager()

  def __repr__(self):
		return '\n package [{}] - {}, {}, {}'.\
      format(self.id,self.name,self.cost,self.available)

# QUERIES:
# Package.objects.create(name='package3',cost=129.99,status=False)
# Package.objects.all().filter(users=User.objects.get(id='1'))
# Package.objects.get(id=2).users.count()
# Package.objects.filter(available=True).values('name','cost','available', n=Count('users')).order_by('n')
