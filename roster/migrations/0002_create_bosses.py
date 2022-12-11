# Generated by Django 4.0.4 on 2022-12-11 04:42

from django.db import migrations
import json

with open("roster/fixtures/bosses.json", "rb") as f:
    data = json.loads(f.read())


data = [dict_.get("fields") for dict_ in data]
boss_names = [item.get("name") for item in data]


def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Boss = apps.get_model("roster", "Boss")

    Boss.objects.using(db_alias).bulk_create(
        [Boss(**parameters) for parameters in data]
    )


def reverse_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Boss = apps.get_model("roster", "Boss")

    Boss.objects.using(db_alias).filter(name__in=boss_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0001_initial"),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_code=reverse_func)]
