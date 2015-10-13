# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 10, 13, 13, 3, 8, 301000, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
    ]
