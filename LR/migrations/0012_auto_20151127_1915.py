# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0011_transporter_stations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='name',
            new_name='label',
        ),
    ]
