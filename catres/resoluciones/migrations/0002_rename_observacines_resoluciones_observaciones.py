# Generated by Django 5.1 on 2024-08-26 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resoluciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resoluciones',
            old_name='observacines',
            new_name='observaciones',
        ),
    ]
