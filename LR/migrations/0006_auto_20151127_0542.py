# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0005_auto_20151127_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=250, choices=[(b'IN', b'India')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=250, choices=[(b'BR', b'Bihar')]),
            preserve_default=True,
        ),
    ]
