# Generated by Django 2.2.24 on 2022-08-26 18:25

from django.db import migrations

import phonenumbers


def normalize_phone_numbers(apps, schema_editor):

    def normalize_number(phone_number: str) -> str:
        parsed_number = phonenumbers.parse(phone_number, 'RU')
        if not phonenumbers.is_valid_number(parsed_number):
            return ''
        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = normalize_number(flat.owners_phonenumber)
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers, move_backward)
    ]
