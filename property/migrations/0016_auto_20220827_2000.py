# Generated by Django 2.2.24 on 2022-08-27 17:00

from django.db import migrations


def add_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            name=flat.owner,
            normalized_phone=flat.owner_pure_phone,
            defaults={
                'phone_number': flat.owner_pure_phone,
            },
        )
        owner.flats.add(flat)


def move_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220827_1957'),
    ]

    operations = [
        migrations.RunPython(add_flats_to_owners, move_backward)
    ]