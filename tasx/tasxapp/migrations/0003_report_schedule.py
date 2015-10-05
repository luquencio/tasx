# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasxapp', '0002_auto_20151005_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='schedule',
            field=models.CharField(max_length=50, default=datetime.datetime(2015, 10, 5, 6, 12, 2, 239674, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
