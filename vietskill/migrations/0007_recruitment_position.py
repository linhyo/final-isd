# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vietskill', '0006_auto_20150112_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='position',
            field=models.CharField(default=datetime.datetime(2015, 1, 13, 6, 8, 32, 723120, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
