# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logreg_app', '0001_initial'),
        ('exam4_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('tasks', models.TextField(max_length=1000)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='logreg_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='new',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='new',
            name='user',
        ),
        migrations.DeleteModel(
            name='New',
        ),
    ]
