# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consignor',
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
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='LR.Address')),
                ('name', models.CharField(max_length=250)),
                ('contactNumber', models.IntegerField()),
                ('contactPerson', models.CharField(max_length=250, null=True, blank=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=('LR.address',),
        ),
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('vanNo', models.CharField(max_length=250, null=True, blank=True)),
                ('name', models.CharField(max_length=250, null=True, blank=True)),
                ('remarks', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForwardingNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billDate', models.DateField()),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('billNo', models.CharField(max_length=250, null=True, blank=True)),
                ('billValue', models.CharField(max_length=250, null=True, blank=True)),
                ('cases', models.CharField(max_length=250, null=True, blank=True)),
                ('marka', models.CharField(max_length=250, null=True, blank=True)),
                ('permitNo', models.CharField(max_length=250, null=True, blank=True)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('consignor', models.ForeignKey(blank=True, to='LR.Consignor', null=True)),
                ('customer', models.ForeignKey(to='LR.Customer')),
                ('transporter', models.ForeignKey(to='LR.Transporter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='LR.Address')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=('LR.address',),
        ),
        migrations.AddField(
            model_name='dispatch',
            name='lr',
            field=models.ManyToManyField(to='LR.ForwardingNote'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='transporter',
            options={},
        ),
    ]
