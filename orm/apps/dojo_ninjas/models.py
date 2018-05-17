# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email_address = models.CharField(max_length=255)
  age = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return '\n( {} {}, {}, {} )'.format(self.first_name,self.last_name,self.email_address,self.age)

  def __str__(self):
    return 'user( {} {}, {}, {})'.format(self.first_name,self.last_name,self.email_address,self.age)

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __repr__(self):
    return '\n( {}, {}, {}, {} )'.format(self.name,self.city,self.state,self.desc)

  def __str__(self):
    return 'dojo( name={}, city={}, state={} )'.format(self.name,self.city,self.state)
	
class Ninja(models.Model):
  dojo_id = models.ForeignKey(Dojo, related_name="ninjas")
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return '\nninja( {} {}, {} )'.format(self.first_name,self.last_name,self.dojo_id)

  def __str__(self):
    return '\nninja( {} {}, dojo={} )'.format(self.first_name,self.last_name,self.dojo_id)

# [FIST MIGRATE CHANGES]
# python manage.py makemigrations
# python manage.py migrate
#
# [USE SHELL TO CREATE INITIAL RECORDS]
# FROM SHELL, i.e. python manage.py shell
# from apps.dojo_ninjas.models import *
#
# User.objects.create(
#  first_name='Jimi', last_name='Hendrix',
#  email_address='jmii@acid.com', age='38'
#  )
# User.objects.create(
#  first_name='Johnny', last_name='Dangerous',
#  email_address='jd@socool.com', age='41'
#  )
# User.objects.create(
#  first_name='Johnny', last_name='Walker',
#  email_address='johnny@walker.com', age='65'
#  )
#
# Dojo.objects.create(
#   name='CodingDojo Sillicon Valley', city='Mountain View', state='CA'
#   )
# Dojo.objects.create(
#   name='CodingDojo Seattle', city='Seattle', state='WA'
#   )
# Dojo.objects.create(
#   name='CodingDojo New York', city='New York', state='NY'
#   )
#
# [SAMPLE TO CREATE NINJA} 
# Ninja.objects.create(
#   first_name='Billy', last_name='Bob', dojo_id=Dojo.objects.get(id=1)
#   )