# Generated by Django 3.0.6 on 2020-06-22 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rozklad', '0004_remove_trozporyadok_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trozporyadok',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 33, 45), max_length=200),
        ),
    ]
