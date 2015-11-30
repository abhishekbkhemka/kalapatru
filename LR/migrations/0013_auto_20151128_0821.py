# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0012_auto_20151127_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='forwardingnote',
            name='transporterStation',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forwardingnote',
            name='billDate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
