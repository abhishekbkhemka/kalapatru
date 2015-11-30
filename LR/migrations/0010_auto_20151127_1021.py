# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0009_auto_20151127_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addressLine1',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True, choices=[(b'IN', b'India')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=250, null=True, choices=[(b'BR', b'Bihar')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='contactNumber',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transporter',
            name='contactNumber',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
