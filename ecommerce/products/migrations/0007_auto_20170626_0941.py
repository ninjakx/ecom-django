# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170626_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='img_name',
            field=models.CharField(max_length=120),
        ),
    ]
