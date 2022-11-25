from django.shortcuts import render, redirect
import requests
from wow_roster.secrets import oauth
from requests.auth import HTTPBasicAuth
from .forms import CharacterForm
from .models import Character

available_roles = {
                    "Warrior": ["dps", "tank"],
                    "Paladin": ["dps", "tank", "healer"],
                    "Hunter": ["dps"],
                    "Rogue": ["dps"],
                    "Priest": ["dps", "healer"],
                    "Shaman": ["dps", "healer"],
                    "Mage": ["dps"],
                    "Warlock": ["dps"],
                    "Monk": ["dps", "tank", "healer"],
                    "Druid": ["dps", "tank", "healer"],
                    "Demon Hunter": ["dps", "tank"],
                    "Death Knight": ["dps", "tank"],
                    "Evoker": ["dps", "healer"]
                  }


def add_character(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            token_response = requests.post('https://oauth.battle.net/token',
                                    auth=HTTPBasicAuth(oauth["id"], oauth["secret"]),
                                    data={"grant_type": "client_credentials"})
            access_token = token_response.json().get("access_token")
            if access_token:
                data = form.cleaned_data
                url = f'https://{data["server"]}.api.blizzard.com/profile/wow/character/{data["realm"]}/{data["character_name"]}/appearance?namespace=profile-{data["server"]}&locale=en_US'
                response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
                if response.status_code < 300:
                    class_name = response.json()['playable_class']["name"]
                    if data["role"] in available_roles[class_name]:
                        character = Character(name=data["character_name"], role=data["role"], realm=data["realm"], server=data["server"])
                        character.save()
                        return redirect("/characters")
                    form.add_error(None, "Role not available")
                else:
                    form.add_error(None, "Character not found")
    else:
        form = CharacterForm()
    return render(request, 'add_character.html', {"form": form})


def list_characters(request):
    characters = Character.objects.all()
    return render(request, 'characters.html', {"characters": characters})
