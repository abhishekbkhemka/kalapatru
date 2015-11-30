# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addressLine1', models.CharField(max_length=250)),
                ('addressLine2', models.CharField(max_length=250, null=True, blank=True)),
                ('area', models.CharField(max_length=250, null=True, blank=True)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250, choices=[(b'IN', b'India')])),
                ('country', models.CharField(max_length=250, choices=[(b'BR', b'Bihar')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='LR.Address')),
                ('name', models.CharField(max_length=250)),
                ('contactNumber', models.IntegerField()),
                ('contactPerson', models.CharField(max_length=250, null=True, blank=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Transporters',
            },
            bases=('LR.address',),
        ),
    ]
