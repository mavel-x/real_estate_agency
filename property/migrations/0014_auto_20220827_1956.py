# Generated by Django 2.2.24 on 2022-08-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220827_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО'),
        ),
    ]
