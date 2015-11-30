# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LR', '0003_consignor_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='consignor',
            name='org',
            field=models.ForeignKey(default=1, to='LR.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='org',
            field=models.ForeignKey(default=1, to='LR.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transporter',
            name='org',
            field=models.ForeignKey(default=1, to='LR.Organization'),
            preserve_default=False,
        ),
    ]
