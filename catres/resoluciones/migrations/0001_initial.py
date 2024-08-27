# Generated by Django 5.1 on 2024-08-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resoluciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('sumario', models.TextField(max_length=1024)),
                ('origen', models.CharField(choices=[('ptn', 'PTN'), ('sptn', 'SPTN')], default='ptn', max_length=4)),
                ('fecha', models.DateField()),
                ('fecha_publicacion', models.DateField()),
                ('observacines', models.TextField()),
            ],
            options={
                'verbose_name': 'Resoluciones',
                'verbose_name_plural': 'Resoluciones',
                'db_table': 'resoluciones',
            },
        ),
    ]
