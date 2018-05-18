# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

# email_regex=r'[^@]+@[^@]+\.[^@]'
name_min = 1; pwmin=5
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pwd_regex = re.compile(r'^[ !A-Za-z0-9@#$%^&=+_-]{8,}$')

class UserManager(models.Manager):
    def basic_validator(self, postData, type):
        errors = {}

        print '\n',"*"*10,' CRUD (def basic-validator)\n'

        if type=='register':
            
            print '***** in REGISTER\n request.POST=', postData

            if email_regex.match(postData['email']):
                if User.objects.filter(email=postData['email']).exists():
                    errors['email'] = '"{}" has already registered.'.format(postData['email'])
            else:
                errors['email']='"{}" is not a valid email address.'.format(postData['email'])
                    
            if not (len(postData['first_name']) >= name_min) and (len(postData['last_name']) >= name_min) :
                errors['name'] = 'The length of first name or last name must be at least {}.'.format(name_min)
            
            if postData['password'] == postData['confirmation']:
                print pwd_regex.match(postData['password'])
                print postData['password']
                if not pwd_regex.match(postData['password']):
                    errors['password']='Password string must be at least {} \
                    of spaces and the acceptable characters: !A-Za-z0-9@#$%^&=+_-"'.format(pwmin)
            else:
                errors['password']='Password and confirmed password do not match.'
                
        elif type=='login':

            print '***** in LOGIN\n request.POST=', postData

            if email_regex.match(postData['email']):
                if User.objects.filter(email=postData['email']).exists():
                    print '*****{} found'.format(postData['email'])
                else:
                    errors['email'] = '"{}" is not yet registered.'.format(postData['email'])
            else:
                errors['email']='"{}" is not a valid email address.'.format(postData['email'])
            
        else:
            errors['validation_type']='unknown validation type'
        
        print errors

        return errors
          

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	objects = UserManager()
	
	def __repr__(self):
		return '\n user ({} {}, {})'.\
        format(self.first_name,self.last_name,self.email)

