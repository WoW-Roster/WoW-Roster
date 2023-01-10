from django.db import models

from roster.querysets import BossQuerySet


class BossManager(models.Manager):
    def get_queryset(self):
        return BossQuerySet(self.model, using=self._db)

    def count_players(self):
        return self.get_queryset().count_players()

    def count_roles(self):
        return self.get_queryset().count_roles()

    def with_buffs(self):
        return self.get_queryset().with_buffs()

