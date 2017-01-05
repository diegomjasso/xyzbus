# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 03:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('camiones', '0004_auto_20161230_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordenadas_rutas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coordenadas', geoposition.fields.GeopositionField(blank=True, max_length=42)),
                ('order', models.IntegerField()),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camiones.Catalogo_rutas')),
            ],
            options={
                'verbose_name_plural': 'Coordenadas de las Rutas',
            },
        ),
    ]
