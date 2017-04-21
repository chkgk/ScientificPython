# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_auto_20160512_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'ordering': ('last_name', 'first_name')},
        ),
    ]
