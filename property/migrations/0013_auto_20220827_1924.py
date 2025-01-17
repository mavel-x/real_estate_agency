# Generated by Django 2.2.24 on 2022-08-27 16:24

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='normalized_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='нормализованный номер телефона'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='номер телефона'),
        ),
    ]
