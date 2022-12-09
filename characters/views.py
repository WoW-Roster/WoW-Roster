import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render

import requests
from characters.forms import CharacterForm
from characters.models import Character
from http import HTTPStatus
from requests.auth import HTTPBasicAuth

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
    "Evoker": ["dps", "healer"],
}


def add_character(request):
    form_class = CharacterForm
    if request.method != "POST":
        return render(request, "add_character.html", {"form": form_class()})
    form = form_class(request.POST)
    if not form.is_valid():
        return render(request, "add_character.html", {"form": form})
    token_response = requests.post(
        "https://oauth.battle.net/token",
        auth=HTTPBasicAuth(settings.WOW_API_CLIENT_ID, settings.WOW_API_CLIENT_SECRET),
        data={"grant_type": "client_credentials"},
    )
    access_token = token_response.json().get("access_token")
    if not access_token:
        return render(request, "add_character.html", {"form": form})
    data = form.cleaned_data
    url = f'https://{data["server"]}.api.blizzard.com/profile/wow/character/{data["realm"]}/{data["character_name"]}/appearance?namespace=profile-{data["server"]}&locale=en_US'
    response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
    if response.status_code == HTTPStatus.NOT_FOUND:
        form.add_error(None, "Character not found")
        return render(request, "add_character.html", {"form": form})

    class_name = response.json()["playable_class"]["name"]
    if not data["role"] in available_roles[class_name]:
        form.add_error(None, "Role not available")
        return render(request, "add_character.html", {"form": form})

    character = Character(
        name=data["character_name"],
        role=data["role"],
        realm=data["realm"],
        server=data["server"],
        game_class=class_name,
    )
    character.save()
    return redirect("/characters")


def delete_character(request):
    if request.method == "DELETE":
        data = json.loads(request.body)
        character_name = data.get("character_name")
        realm = data.get("realm")
        server = data.get("server")
        if not character_name or not realm or not server:
            return HttpResponse(status=400)
        Character.objects.filter(
            name=character_name, realm=realm, server=server
        ).delete()
        return HttpResponse(status=200)
    return HttpResponse(status=400)


def change_character_role(request):
    if request.method == "POST":
        data = json.loads(request.body)
        character_name = data.get("character_name")
        realm = data.get("realm")
        server = data.get("server")
        role = data.get("role")
        if not character_name or not realm or not server or not role:
            return HttpResponse(status=400)

        character = Character.objects.filter(
            name=character_name, realm=realm, server=server
        ).first()
        if not character or role not in available_roles[character.game_class]:
            return HttpResponse(status=400)
        character.role = role
        character.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)


def list_characters(request):
    characters = Character.objects.all()
    characters_jinja = [
        {
            "character": character,
            "available_roles": available_roles[character.game_class],
        }
        for character in characters
    ]
    return render(request, "characters.html", {"data": characters_jinja})
