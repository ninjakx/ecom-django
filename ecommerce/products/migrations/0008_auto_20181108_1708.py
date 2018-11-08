# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20170626_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='imageslide',
            field=models.ImageField(upload_to='sliders/'),
        ),
    ]
