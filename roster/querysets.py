from django.db import models
from django.db.models import Count, Q

from characters.models import Character


class BossQuerySet(models.QuerySet):
    def count_players(self):
        return self.annotate(players_count=Count("players"))

    def count_tanks(self):
        return self.annotate(
            tank_count=Count("players", filter=Q(players__role=Character.ROLES.TANK))
        )

    def count_healers(self):
        return self.annotate(
            healer_count=Count(
                "players", filter=Q(players__role=Character.ROLES.HEALER)
            )
        )

    def count_dps(self):
        return self.annotate(
            dps_count=Count("players", filter=Q(players__role=Character.ROLES.DPS))
        )

    def count_roles(self):
        return self.count_tanks().count_healers().count_dps()

    def check_bloodlust_buff(self):
        return self.annotate(
            bloodlust_buff=Count(
                "players",
                filter=Q(players__game_class=Character.CLASSES.MAGE)
                | Q(players__game_class=Character.CLASSES.HUNTER)
                | Q(players__game_class=Character.CLASSES.SHAMAN)
                | Q(players__game_class=Character.CLASSES.EVOKER),
            )
        )

    def check_attack_power_buff(self):
        return self.annotate(
            attack_power_buff=Count(
                "players", filter=Q(players__game_class=Character.CLASSES.WARRIOR)
            )
        )

    def check_intellect_buff(self):
        return self.annotate(
            intellect_buff=Count(
                "players", filter=Q(players__game_class=Character.CLASSES.MAGE)
            )
        )

    def check_stamina_buff(self):
        return self.annotate(
            stamina_buff=Count(
                "players", filter=Q(players__game_class=Character.CLASSES.PRIEST)
            )
        )

    def check_magic_damage_buff(self):
        return self.annotate(
            magic_damage_buff=Count(
                "players", filter=Q(players__game_class=Character.CLASSES.DEMON_HUNTER)
            )
        )

    def check_physical_damage_buff(self):
        return self.annotate(
            physical_damage_buff=Count(
                "players", filter=Q(players__game_class=Character.CLASSES.MONK)
            )
        )

    def check_devotion_aura(self):
        return self.annotate(
            devo_aura=Count(
                "players", filter=Q(players__game_class=Character.CLASSES.PALADIN)
            )
        )

    def with_buffs(self):
        return (
            self.check_bloodlust_buff()
            .check_attack_power_buff()
            .check_intellect_buff()
            .check_stamina_buff()
            .check_magic_damage_buff()
            .check_physical_damage_buff()
            .check_devotion_aura()
        )
