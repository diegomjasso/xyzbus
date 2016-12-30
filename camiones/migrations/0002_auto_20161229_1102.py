# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('camiones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corridas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_final', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='rutas',
            name='punto_final',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
        migrations.AddField(
            model_name='rutas',
            name='punto_inicio',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
        migrations.AddField(
            model_name='corridas',
            name='ruta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camiones.Rutas'),
        ),
    ]