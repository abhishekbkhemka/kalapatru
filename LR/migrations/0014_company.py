# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0013_auto_20151128_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='LR.Address')),
                ('label', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=('LR.address',),
        ),
    ]
