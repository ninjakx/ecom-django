# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170626_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='imageslide',
            field=models.ImageField(upload_to='/slider'),
        ),
    ]
