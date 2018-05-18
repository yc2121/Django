#-*- coding: utf-8 -*-
from django import forms
from django.db import models

class LoginForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    email = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
