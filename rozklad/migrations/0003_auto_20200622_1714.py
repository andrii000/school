# Generated by Django 3.0.6 on 2020-06-22 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rozklad', '0002_urtimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='trozporyadok',
            name='time_end',
            field=models.TimeField(default=django.utils.timezone.now, max_length=200),
        ),
        migrations.AddField(
            model_name='trozporyadok',
            name='time_start',
            field=models.TimeField(default=django.utils.timezone.now, max_length=200),
        ),
        migrations.AlterField(
            model_name='trozporyadok',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, max_length=200),
        ),
    ]
