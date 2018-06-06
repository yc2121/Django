# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.db import models
import re, bcrypt, time

# # email_regex=r'[^@]+@[^@]+\.[^@]'
name_regex = re.compile(r'^[a-zA-Z]{3,}$')
username_regex = re.compile(r'^[a-zA-Z0-9]{3,}$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pwd_regex = re.compile(r'^[ !A-Za-z0-9@#$%^&=+_-]{3,}$')

class UserManager(models.Manager):

  def basic_validator(self, postData):
      
    errors = {}
    print '\n',"*"*10,' def basic-validator)\n'

    # Already registered
    if User.objects.filter(username=postData['username']).exists():
      errors['username'] = '"{}" has already registered.'.format(postData['username'])

    # Name format
    if not name_regex.match(postData['name']):
      errors['name']='"{}" must be with 3 or more\
       of the acceptable characters:A-Za-z.'.format(postData['name'])
                
    # Username format
    if not username_regex.match(postData['username']):
      errors['username']='"{}" must be with 3 or more\
       of the acceptable characters: A-Za-z0-9.'.format(postData['username'])
        
    # Password confirmation
    if postData['password'] != postData['confirmation']:
      errors['password']='Password and confirmed password do not match.'
    
    # Password complexities
    if not pwd_regex.match(postData['password']):
      errors['password']='Password string must be with 3 or more\
       of the acceptable characters: !A-Za-z0-9@#$%^&=+_-"'

    # Date 
    if time.strptime(postData['doh'],'%Y-%m-%d') > time.localtime():
      errors['doh']='Date Hire can not be a future date'
    
    if not time.strptime(postData['doh'],'%Y-%m-%d'):
      errors['doh']='Please specify Hired Date.'
       
    print 'in User basic vlaidator, Errors = {}'.format(errors)

    return errors
      
class User(models.Model):
  name = models.CharField(max_length=30)
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=30)
  doh = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  objects = UserManager()
  
  def __repr__(self):
		return '\n user [{}] - {}, {}, {}'.\
      format(self.id,self.name,self.username,self.doh)

class ItemManager(models.Manager):

  def basic_validator(self, postData):
      
    errors = {}
    print '\n',"*"*10,' def basic-validator)\n'

    if postData['item']=='':
      errors['item']='Please specify the item name'
      
    print 'Errors = {}'.format(errors)

    return errors

class Item(models.Model):
  item = models.CharField(max_length=30)
  users = models.ManyToManyField(User, related_name='added_by')
  user = models.ForeignKey(User, related_name='created_by')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = ItemManager()

  def __repr__(self):
		return '\n item [{}] - {}, {}'.\
      format(self.id, self.item, self.created_at)
