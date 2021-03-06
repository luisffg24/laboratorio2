# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-22 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ante_clinicos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.AntecedenteClinico')),
                ('ante_familiares', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.AntecedenteFamiliar')),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente')),
            ],
        ),
    ]
