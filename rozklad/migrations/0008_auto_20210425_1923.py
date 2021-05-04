# Generated by Django 2.2.20 on 2021-04-25 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rozklad', '0007_auto_20200622_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trozklad',
            name='nlesson',
        ),
        migrations.AddField(
            model_name='trozklad',
            name='nomer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rozklad.Urtimes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urtimes',
            name='nur',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]