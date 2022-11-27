from django.db import models
from characters.models import Character

class Boss(models.Model):
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(Character, null=True, blank=True)
