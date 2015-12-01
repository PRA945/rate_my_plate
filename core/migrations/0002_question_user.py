# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default='1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
