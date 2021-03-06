# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-21 00:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0002_imagenes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagenes',
            options={'ordering': ['fechaSubida'], 'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AlterField(
            model_name='imagenes',
            name='detalle',
            field=models.CharField(default='Sin detalles', max_length=250),
        ),
        migrations.AlterField(
            model_name='imagenes',
            name='fechaCaptura',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='imagenes',
            name='fechaSubida',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 19, 39, 53, 129130)),
        ),
    ]
