# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0008_auto_20151127_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forwardingnote',
            name='billDate',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forwardingnote',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forwardingnote',
            name='fnDate',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
