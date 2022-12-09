from django.db import models
from characters.types import RoleTypes, ClassTypes

# Create your models here.

class Character(models.Model):
    ROLES = RoleTypes()
    CLASSES = ClassTypes()

    name = models.CharField(max_length=24)
    game_class = models.CharField(max_length=20)
    role = models.CharField(max_length=6)
    realm = models.CharField(max_length=40)
    server = models.CharField(max_length=2)
    def __str__(self) -> str:
        return f"{self.name}-{self.role}"

