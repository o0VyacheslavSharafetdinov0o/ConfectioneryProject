# Generated by Django 3.0.3 on 2020-10-05 05:59

import Backend.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='client',
            managers=[
                ('objects', Backend.models.ClientManager()),
            ],
        ),
    ]
