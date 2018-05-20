from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    datetime = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.description
