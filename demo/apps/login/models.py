# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt
email_regex=r'[^@]+@[^@]+\.[^@]'

class UserManager(models.Manager):
    # Manager is the validator
    def basic_validator(self, postData):
        errors = {}
        if not re.match(email_regex,postData['email']):
            errors['email']='bad email address'
        if len(postData['first_name']) < 5:
            errors["first_name"] = "First name erro message"
        if len(postData['last_name']) < 5:
            errors["last_name"] = "Last name erro message"
        if len(postData['email']) < 10:
            errors["email"] = "Email error messae"
        if len(postData['password']) < 10:
            errors["password"] = "Password error messae"
        if len(postData['confirmation']) < 10:
            errors["confirmation"] = "Confirmation error messae"
        return errors

class User(models.Model):
	full_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	objects = UserManager()
	
	def __repr__(self):
		return '\n user (	{}, {} )'.format(self.full_name,self.email)

