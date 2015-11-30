# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0010_auto_20151127_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='transporter',
            name='stations',
            field=models.ManyToManyField(to='LR.Station'),
            preserve_default=True,
        ),
    ]
