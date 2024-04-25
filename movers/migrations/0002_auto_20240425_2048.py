# Generated by Django 3.2.1 on 2024-04-25 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='moving_from',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='moving_to',
        ),
        migrations.AddField(
            model_name='quotation',
            name='destination_address',
            field=models.CharField(default=1, max_length=100, verbose_name='Moving To'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotation',
            name='mover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotations', to='movers.mover'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='source_address',
            field=models.CharField(default=1, max_length=100, verbose_name='Moving From'),
            preserve_default=False,
        ),
    ]
