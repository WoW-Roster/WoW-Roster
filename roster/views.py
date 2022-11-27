from django.shortcuts import render
from characters.views import *
from django.views.generic.list import ListView
from roster.models import Boss
from characters.models import Character
from django.db.models import Count, Q
from django.views.generic.edit import UpdateView
from roster.forms import BossRosterForm
from django.urls import reverse

def players_selection(request):
    characters = Character.objects.all()
    characters_jinja = [
        {
            "character": character,
            "available_roles": available_roles[character.game_class],
        }
        for character in characters
    ]
    return render(
        request,
        "players_selection.html",
        {"data": characters_jinja},
    )


class BossListView(ListView):
    model = Boss
    template_name = "players_selection.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["characters"] = Character.objects.all().values_list("name")
    #     context["tank_count"] = Character.objects.filter(role="tank").count()
    #     context["healer_count"] = Character.objects.filter(role="healer").count()
    #     context["dps_count"] = Character.objects.filter(role="dps").count()
    #     return context

    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context["characters"] = Character.objects.all().values_list("name")
    #     role_count_dict = {"tank_count": Character.objects.filter(role="tank").count(),
    #     "healer_count": Character.objects.filter(role="healer").count(),
    #     "dps_count": Character.objects.filter(role="dps").count()}
    #     context.update(role_count_dict)
    #     return context

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