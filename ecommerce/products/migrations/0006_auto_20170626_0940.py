# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170626_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='img_name',
            field=models.CharField(max_length=120, default=False),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='imageslide',
            field=models.ImageField(upload_to='slider/'),
        ),
    ]
