from django import forms
from roster.models import Boss
from characters.models import Character

class BossRosterForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(queryset=Character.objects.all().order_by('-role'))
    class Meta:
        model = Boss
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(BossRosterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        