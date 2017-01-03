# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pasajeros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='edad',
        ),
        migrations.AddField(
            model_name='perfil',
            name='fecha_de_nacimiento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='movimientos',
            name='tipo_movimiento',
            field=models.CharField(choices=[('1', 'Ingreso'), ('2', 'Descuento'), ('3', 'Abono')], max_length=140),
        ),
    ]
