# Generated by Django 2.2.24 on 2022-08-26 19:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220826_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=200, verbose_name='номер телефона')),
                ('normalized_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='нормализованный номер телефона')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='квартиры в собственности')),
            ],
        ),
    ]