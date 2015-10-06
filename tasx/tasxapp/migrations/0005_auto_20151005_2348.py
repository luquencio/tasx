# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasxapp', '0004_auto_20151005_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('home_phone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comments',
            name='client',
            field=models.ForeignKey(to='tasxapp.ProfileClient'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='client',
            field=models.ForeignKey(to='tasxapp.ProfileClient'),
        ),
        migrations.AlterField(
            model_name='report',
            name='client',
            field=models.ForeignKey(to='tasxapp.ProfileClient'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
