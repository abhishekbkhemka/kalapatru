# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0004_auto_20151126_0637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispatch',
            old_name='lr',
            new_name='forwardingNote',
        ),
        migrations.AddField(
            model_name='forwardingnote',
            name='isDispatched',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
