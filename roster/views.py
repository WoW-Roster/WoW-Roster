from django.shortcuts import render
from characters.views import *
from django.views.generic.list import ListView
from roster.models import Boss
from characters.models import Character

def bosses_selection(request):
    bosses_file = open('./bosses.txt', 'r')
    data = bosses_file.read()
    list = data.split('\n')
    bosses_file.close()
    return render(request, 'bosses_selection.html', {'list': list})

def players_selection(request):
    characters = Character.objects.all()
    characters_jinja = [{"character": character, "available_roles": available_roles[character.game_class]} for character in characters]    
    return render(request, 'players_selection.html', {"data": characters_jinja},)

class BossListView(ListView):
    model = Boss
    template_name = 'players_selection.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["CharacterListView"] = Character.objects.all().values_list("name", "role")
        return context