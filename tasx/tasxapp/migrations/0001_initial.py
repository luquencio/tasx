# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('home_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('rate', models.IntegerField()),
                ('user', models.ForeignKey(to='tasxapp.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(to='tasxapp.Client')),
                ('employee', models.ForeignKey(to='tasxapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('R', 'Reportado'), ('PP', 'Esperando Primer pago'), ('P', 'Servicio en Proceso'), ('SP', 'Esperando Segundo Pago'), ('C', 'Completado')], max_length=5)),
                ('descr', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('EB', 'Ebanisteria'), ('PL', 'Plomeria'), ('EL', 'Electricidad')], max_length=5)),
                ('photo', models.ImageField(null=True, blank=True, upload_to='media/reports')),
                ('client', models.ForeignKey(to='tasxapp.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ReportResult',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(to='tasxapp.Employee')),
                ('report', models.ForeignKey(to='tasxapp.Report')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='report',
            field=models.ForeignKey(to='tasxapp.Report'),
        ),
    ]
