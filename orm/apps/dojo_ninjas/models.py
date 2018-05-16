# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __repr__(self):
    return '\n({},{},{})'.format(self.name,self.city,self.state)

  def __str__(self):
    return 'dojo(name={},city={},state={})'.format(self.name,self.city,self.state)
	
class Ninja(models.Model):
  dojo_id = models.ForeignKey(Dojo, related_name="ninjas")
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return 'ninja ({},{},{})'.format(self.name,self.city,self.state)

  def __str__(self):
    return 'ninja(dojo_id={},first_name={},last_name={})'.format(self.name,self.city,self.state)

# [FIST MIGRATE CHANGES]
# python manage.py makemigrations
# python manage.py migrate
#
# [USE SHELL TO CREATE INITIAL RECORDS]
# FROM SHELL, i.e. python manage.py shell
# from apps.dojo_ninjas.models import *
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