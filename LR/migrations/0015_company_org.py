# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0014_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='org',
            field=models.ForeignKey(default=1, to='LR.Organization'),
            preserve_default=False,
        ),
    ]
