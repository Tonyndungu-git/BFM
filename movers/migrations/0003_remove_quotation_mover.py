# Generated by Django 3.2.1 on 2024-04-25 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movers', '0002_auto_20240425_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='mover',
        ),
    ]