from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.db import models
import re, bcrypt, time

nameMin = 3; pwdMin = 3
# # email_regex=r'[^@]+@[^@]+\.[^@]'
name_regex = re.compile(r'^[a-zA-Z]{'+str(nameMin)+',}$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pwd_regex = re.compile(r'^[ !A-Za-z0-9@#$%^&=+_-]{'+str(pwdMin)+',}$')

def basic_validator(self, postData, forThis):
      
    errors = {}
    print '\n',"*"*10,' def basic-validator)\n'
    print 'Validating {}'.format(forThis)

    # Email format
    if not email_regex.match(postData['email']):
      errors['email']='This "{}" format is not valid.'.format(postData['email'])

    if forThis == 'login':

      if User.objects.filter(email=postData['email']).exists():
        print 'This "{}" is found.'.format(postData['email'])
        u=User.objects.get(email=postData['email'])
        print 'Checking password for {}'.format(u.name)
        if bcrypt.checkpw(postData['password'].encode(), u.password.encode()):
          print 'Passowrd matched for {}'.format(u.name)
        else:
          print "Incorrect password"
          errors['password'] = 'Incorrect password!'
      else:
        errors['email'] = '{} is not found.'.format(postData['email'])

    elif forThis == 'register':
      if User.objects.filter(email=postData['email']).exists():
        errors['email']='This "{}" has already registered.'.format(postData['email'])

      # Password confirmation
      if postData['password'] != postData['confirmation']:
        errors['password']='Password and confirmed password do not match.'
      
      # Password complexities
      if not pwd_regex.match(postData['password']):
        errors['password']='Password string must be with {} or more\
        of the acceptable characters: !A-Za-z0-9@#$%^&=+_-"'.format(pwdMin)

      # Date & Time (CHANGE THE CRITERIA AS APPLICABLE)
      thisDate = time.strptime(postData['theDate'],'%Y-%m-%d')
      if thisDate < time.localtime(): # for making an appointment
        errors['theDate']='A past date is not applicable.'
      else:
        if not time.strptime(postData['theTime'],'%H:%M') < time.localtime():
          errors['theTime']='Apointment can not be in the past.'
    else:    
      print '\n',"*"*10,' Issue with validation type)\n'

    print 'in User basic vlaidator, \nErrors = {}'.format(errors)

    return errors

# class User(models.Model):

  # email = models.CharField(max_length=50)
  # .....
  # created_at = models.DateTimeField(auto_now_add=True)
  # updated_at = models.DateTimeField(auto_now=True)
  
  # objects = UserManager()
  
  # def __repr__(self):
  #   return '\n user [{}] - {}'.format(self.id,self.name)
