from django.db import models

from characters.models import Character
from roster.managers import BossManager


class Boss(models.Model):
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(Character)

    objects = BossManager()
