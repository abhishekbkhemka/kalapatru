# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0015_company_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch',
            name='date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
