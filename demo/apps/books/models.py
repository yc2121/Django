# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# class BlogManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['first_name']) < 5:
#             errors["first_name"] = "First name erro message"
#         if len(postData['last_name']) < 5:
#             errors["last_name"] = "Last name erro message"
#         if len(postData['email']) < 10:
#             errors["email"] = "Email error messae"
#         if len(postData['password']) < 10:
#             errors["password"] = "Password error messae"
#         if len(postData['confirmation']) < 10:
#             errors["confirmation"] = "Confirmation error messae"
#         return errors

class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	# objects = BlogManager()
	
	def __repr__(self):
		return 'book (	{},\n {} )'.format(self.name,self.desc)

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name='authors')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	# objects = BlogManager()
	
	def __repr__(self):
		return '\n user (	[{}] {} {}, {},\n created_at: {}, updated_at: {} )'.\
		format(self.id,self.first_name,self.last_name,self.email,self.created_at,self.updated_at)


