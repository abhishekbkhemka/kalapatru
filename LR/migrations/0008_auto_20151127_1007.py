# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0007_auto_20151127_0658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forwardingnote',
            old_name='description',
            new_name='comments',
        ),
        migrations.AddField(
            model_name='forwardingnote',
            name='fnDate',
            field=models.DateField(default=datetime.datetime(2015, 11, 27, 10, 7, 14, 588030, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
