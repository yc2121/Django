# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.db import models
import re, bcrypt

# email_regex=r'[^@]+@[^@]+\.[^@]'
name_min = 2; pwmin=8
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pwd_regex = re.compile(r'^[ !A-Za-z0-9@#$%^&=+_-]{8,}$')

class UserManager(models.Manager):
    def basic_validator(self, postData, type):
        errors = {}

        print '\n',"*"*10,' def basic-validator)\n'

        if type=='register':
            
            print '***** type==REGISTER\n request.POST=', postData

            if email_regex.match(postData['email']):
                if User.objects.filter(email=postData['email']).exists():
                    errors['email'] = '"{}" has already registered.'.format(postData['email'])
            else:
                errors['email']='"{}" is not a valid email address.'.format(postData['email'])
                    
            if not (len(postData['name']) >= name_min) :
                errors['name'] = 'The length of a name must be at least {}.'.format(name_min)
            
            if postData['password'] == postData['confirmation']:
                print pwd_regex.match(postData['password'])
                print postData['password']
                if not pwd_regex.match(postData['password']):
                    errors['password']='Password string must be with no space and at least {} \
                    of the acceptable characters: !A-Za-z0-9@#$%^&=+_-"'.format(pwmin)
            else:
                errors['password']='Password and confirmed password do not match.'
                
        elif type=='login':

            print '***** type==LOGIN\n request.POST=', postData

            if email_regex.match(postData['email']):
                if User.objects.filter(email=postData['email']).exists():
                  print '*****{} found'.format(postData['email'])
                  context={ 'name':postData['email'] }
                  if bcrypt.checkpw( postData['password'].encode(), 
                  (User.objects.get(email=postData['email']).password).encode() ):
                    print 'Passowrd matched for {}'.format(postData['email'])
                  else:
                    errors['password'] = 'Incorrect password!'
                else:
                    errors['email'] = '"{}" is not yet registered.'.format(postData['email'])
            else:
                errors['email']='"{}" is not a valid email address.'.format(postData['email'])
            
        else:
            errors['validation_type']='unknown validation type'
        
        print 'Errors = {}'.format(errors)

        return errors
          
class User(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	dob = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	objects = UserManager()
	
	def __repr__(self):
		return '\n user [{}] - {}, {}, {}'.\
        format(self.id,self.name,self.email,self.dob)

class Appointment(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    thedate = models.DateField()
    thetime = models.TimeField()
    user = models.ForeignKey(User, related_name='has_appointments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __repr__(self):
		return '\n Appointment [{}] - {}, {}, {}, {}'.\
        format(self.id, self.task,self.status,self.thedate,self.thetime)

