# Generated by Django 5.1 on 2024-08-26 18:24

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resoluciones', '0006_remove_resoluciones_tsbuscar'),
    ]

    operations = [
        migrations.AddField(
            model_name='resoluciones',
            name='tsbuscar',
            field=django.contrib.postgres.search.SearchVectorField(blank=True, null=True),
        ),
    ]
