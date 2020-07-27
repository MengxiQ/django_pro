from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)