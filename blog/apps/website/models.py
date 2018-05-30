# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


class Person(models.Model):
  name=models.CharField(max_length=30)
  friends = models.ManyToManyField("self")

  def __repr__(self):
      return self.name

