# Generated by Django 5.1.4 on 2024-12-30 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inflow',
            options={'ordering': ['-created_at'], 'verbose_name': 'Entrada', 'verbose_name_plural': 'Entradas'},
        ),
    ]
