# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re,  bcrypt
email_regex=r'[^@]+@[^@]+\.[^@]'

class UserManager(models.Manager):
    def basic_validator(self, postData, type):
        errors = {}
        print '\n',"*"*10,' SAMPLE (def basic-validator)\n'
        if type=='registeration':
            print 'postData["email_addr"] = ',postData['email_addr']
            if not re.match(email_regex,postData['email_addr']):
                errors['email_addr']='bad email address'
            if len(postData['first_name']) < 5:
                errors["first_name"] = "First name error message"
            if len(postData['last_name']) < 5:
                errors["last_name"] = "Last name error message"
            if len(postData['pwd']) < 5:
                errors["pwd"] = "Password error messae"
            return errors
        elif type=='login':
            print 'postData["email_id"] = ',postData['email_addr']
            if not re.match(email_regex,postData['email_id']):
                errors['email_id']='bad email address'
            if len(postData['pwd']) < 5:
                errors["pwd"] = "Password error messae"
        else:
            errors['validation_type']='unknown validation type'

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

