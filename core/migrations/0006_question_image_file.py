# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151205_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image_file',
            field=models.ImageField(null=True, upload_to=core.models.upload_to_location, blank=True),
        ),
    ]
