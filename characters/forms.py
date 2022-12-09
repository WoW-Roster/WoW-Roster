from django import forms


class CharacterForm(forms.Form):
    server = forms.ChoiceField(
        label="Server",
        choices=[("eu", "eu"), ("us", "us"), ("kr", "kr"), ("tw", "tw"), ("cn", "cn")],
    )
    realm = forms.CharField(label="Realm", max_length=40)
    character_name = forms.CharField(label="Character", max_length=24)
    role = forms.ChoiceField(
        label="Role", choices=[("tank", "tank"), ("healer", "healer"), ("dps", "dps")]
    )
