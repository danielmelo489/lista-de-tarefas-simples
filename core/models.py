from tabnanny import check
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
    date_create = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)