# Generated by Django 2.2.24 on 2022-08-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220826_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='active',
            field=models.BooleanField(db_index=True, verbose_name='Активно ли объявление'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='living_area',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='количество жилых кв. метров'),
        ),
    ]
