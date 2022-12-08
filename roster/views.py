from django.views.generic.list import ListView
from roster.models import Boss
from django.db.models import Count, Q
from django.views.generic.edit import UpdateView
from roster.forms import BossRosterForm
from django.urls import reverse


class BossListView(ListView):
    model = Boss
    template_name = "players_selection.html"

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.annotate(
            players_count=Count("players"),
            tank_count=Count("players", filter=Q(players__role="tank")),
            healer_count=Count("players", filter=Q(players__role="healer")),
            dps_count=Count("players", filter=Q(players__role="dps")),
        )
        return queryset


class BossUpdateView(UpdateView):
    model = Boss
    form_class = BossRosterForm
    template_name: str = "boss_update.html"

    def get_success_url(self) -> str:
        return reverse("boss_list_view")
