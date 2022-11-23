from django.shortcuts import render
import requests
from wow_roster.secrets import oauth
from requests.auth import HTTPBasicAuth


regions = ["us", "eu", "kr", "tw", "cn"]


def add_character(request):
    response = requests.post('https://oauth.battle.net/token',
                             auth=HTTPBasicAuth(oauth["id"], oauth["secret"]),
                             data={"grant_type": "client_credentials"})
    access_token = response.json().get("access_token")
    response = requests.get('https://eu.api.blizzard.com/profile/wow/character/burning-legion/oliwciaa/appearance?namespace=profile-eu&locale=en_US',
                            headers={"Authorization": f"Bearer {access_token}"})
    html = response.json()['playable_class']
    return render(request, 'index.html', html)
