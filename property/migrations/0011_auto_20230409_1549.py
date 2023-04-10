# Generated by Django 2.2.24 on 2023-04-09 12:49

from django.db import migrations


def update_flats_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all().iterator():
        flats = Flat.objects.filter(
            owner=owner.owner,
            owners_phonenumber=owner.owners_phonenumber
        )
        owner.flats.set(flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230408_1543'),
    ]

    operations = [
        migrations.RunPython(update_flats_owner)
    ]