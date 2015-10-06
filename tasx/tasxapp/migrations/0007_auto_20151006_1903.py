# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasxapp', '0006_auto_20151006_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(to='tasxapp.ProfileClient', null=True),
        ),
    ]
