from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=24)
    game_class = models.CharField(max_length=20)
    role = models.CharField(max_length=6)
    realm = models.CharField(max_length=40)
    server = models.CharField(max_length=2)
    def __str__(self) -> str:
        return f"{self.name}-{self.role}"
