# Generated by Django 3.2.1 on 2024-04-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movers', '0003_remove_quotation_mover'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
