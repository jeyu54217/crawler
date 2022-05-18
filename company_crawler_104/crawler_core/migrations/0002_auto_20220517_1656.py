# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='selected_list',
        ),
        migrations.RemoveField(
            model_name='result_list',
            name='user_selected',
        ),
        migrations.AddField(
            model_name='result_list',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='result_list',
            name='user_note',
            field=models.TextField(blank=True, null=True, default=''),
        ),
    ]
