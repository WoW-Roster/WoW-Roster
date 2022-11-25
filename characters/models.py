from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=24)
    role = models.CharField(max_length=6)
    realm = models.CharField(max_length=40)
    server = models.CharField(max_length=2)
