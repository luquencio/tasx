# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasxapp', '0005_auto_20151005_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='client',
            new_name='user',
        ),
    ]
