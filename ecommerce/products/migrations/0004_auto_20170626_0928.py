# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_sliderimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='imageslide',
            field=models.ImageField(upload_to='\\slider'),
        ),
    ]
