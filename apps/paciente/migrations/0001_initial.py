# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-22 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
        ('tratamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedenteClinico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=100)),
                ('fecha_registro', models.DateField()),
                ('medico_tratante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.Medico')),
                ('tratamiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tratamiento.Tratamiento')),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteFamiliar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=100)),
                ('fecha_aproximada', models.DateField()),
                ('parentesco', models.CharField(max_length=20)),
                ('tratamiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tratamiento.Tratamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=12)),
                ('peso', models.IntegerField()),
                ('estatura', models.IntegerField()),
            ],
        ),
    ]
