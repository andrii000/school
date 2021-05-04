# Generated by Django 2.2.20 on 2021-05-03 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rozklad', '0008_auto_20210425_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tlessons',
            name='classroom_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rozklad.Classroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tlessons',
            name='teacher_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rozklad.Teacher'),
            preserve_default=False,
        ),
    ]
