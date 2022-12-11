from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from roster.forms import BossRosterForm
from roster.models import Boss


class BossListView(ListView):
    model = Boss
    template_name = "bosses_list.html"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related("players")
            .count_players()
            .count_roles()
            .with_buffs()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["boss_names"] = self.get_queryset().values_list("name", flat=True)
        return context


class BossUpdateView(UpdateView):
    model = Boss
    form_class = BossRosterForm
    template_name: str = "boss_update.html"

    def get_success_url(self) -> str:
        return reverse("roster:boss_list_view")
