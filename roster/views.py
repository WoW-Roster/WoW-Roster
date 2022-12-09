from django.views.generic.list import ListView
from roster.models import Boss
from django.db.models import Count, Q
from django.views.generic.edit import UpdateView
from roster.forms import BossRosterForm
from django.urls import reverse
from characters.models import Character


class BossListView(ListView):
    model = Boss
    template_name = "players_selection.html"

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.annotate(
            players_count=Count("players"),
            tank_count=Count("players", filter=Q(players__role=Character.ROLES.TANK)),
            healer_count=Count("players", filter=Q(players__role=Character.ROLES.HEALER)),
            dps_count=Count("players", filter=Q(players__role=Character.ROLES.DPS)),
            bloodlust_buff=Count("players", filter=Q(players__game_class=Character.CLASSES.MAGE) | Q(players__game_class=Character.CLASSES.HUNTER) | Q(players__game_class=Character.CLASSES.SHAMAN) | Q(players__game_class=Character.CLASSES.EVOKER)),
            attack_power_buff=Count("players", filter=Q(players__game_class=Character.CLASSES.WARRIOR)),
            intellect_buff=Count("players", filter=Q(players__game_class=Character.CLASSES.MAGE)),
            stamina_buff=Count("players", filter=Q(players__game_class=Character.CLASSES.PRIEST)),
            magic_damage_buff=Count("players", filter=Q(players__game_class=Character.CLASSES.DEMON_HUNTER)),
            physical_damage_buff=Count("players", filter=Q(players__game_class=Character.CLASSES.MONK)),
            devo_aura=Count("players", filter=Q(players__game_class=Character.CLASSES.PALADIN)),
        )
        return queryset


class BossUpdateView(UpdateView):
    model = Boss
    form_class = BossRosterForm
    template_name: str = "boss_update.html"

    def get_success_url(self) -> str:
        return reverse("boss_list_view")
