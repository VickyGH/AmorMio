# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-20 03:08
from __future__ import unicode_literals

import Apps.Administrador.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(default='fotos/None/no-img.jpg', upload_to='fotos/%Y/%m/%d')),
                ('fechaSubida', models.DateField()),
                ('fechaCaptura', models.DateField()),
                ('personaUser', models.CharField(max_length=250, verbose_name=Apps.Administrador.models.Personas)),
                ('detalle', models.CharField(default=False, max_length=250)),
                ('personasFoto', models.ManyToManyField(to='Administrador.Personas')),
                ('tag', models.ManyToManyField(to='Administrador.Tags')),
            ],
            options={
                'ordering': ['detalle'],
                'verbose_name_plural': 'Imagenes',
            },
        ),
    ]
