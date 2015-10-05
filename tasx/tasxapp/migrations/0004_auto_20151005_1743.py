# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasxapp', '0003_report_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('rental_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('report', models.ForeignKey(to='tasxapp.Report')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('home_phone', models.CharField(max_length=11)),
                ('code', models.CharField(max_length=11)),
                ('photo', models.ImageField(upload_to='media/staff')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50, choices=[('P', 'Prestado'), ('D', 'Disponible'), ('DD', 'Defectuosa'), ('R', 'En reparacion')])),
                ('tool_rental', models.ManyToManyField(to='tasxapp.Rental')),
            ],
        ),
        migrations.CreateModel(
            name='ToolRental',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('rental', models.ForeignKey(to='tasxapp.Rental')),
                ('tool', models.ForeignKey(to='tasxapp.Tool')),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='reportresult',
            name='employee',
        ),
        migrations.AddField(
            model_name='comments',
            name='client',
            field=models.ForeignKey(to='tasxapp.Client', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='company_percentage',
            field=models.IntegerField(default=0.2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to='tasxapp.TechnicalStaff'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='rental',
            name='tech',
            field=models.ForeignKey(to='tasxapp.TechnicalStaff'),
        ),
        migrations.AddField(
            model_name='payment',
            name='tech',
            field=models.ForeignKey(to='tasxapp.TechnicalStaff', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportresult',
            name='tech',
            field=models.ForeignKey(to='tasxapp.TechnicalStaff', default=None),
            preserve_default=False,
        ),
    ]
