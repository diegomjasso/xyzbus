# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 19:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo_rutas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_camion', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Catálogo de Rutas',
            },
        ),
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruta', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Rutas',
            },
        ),
        migrations.CreateModel(
            name='Rutas_favoritas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camiones.Rutas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Rutas Favoritas',
            },
        ),
        migrations.AddField(
            model_name='catalogo_rutas',
            name='ruta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camiones.Rutas'),
        ),
    ]
