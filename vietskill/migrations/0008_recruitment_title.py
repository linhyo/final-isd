# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vietskill', '0007_recruitment_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 1, 13, 6, 35, 59, 212332, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
