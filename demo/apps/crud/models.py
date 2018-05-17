# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
	
class User(models.Model):
	full_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	def __repr__(self):
		return '\n user (	{}, {} )'.format(self.full_name,self.email)


