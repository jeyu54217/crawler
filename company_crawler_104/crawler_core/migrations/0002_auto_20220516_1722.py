# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='selected_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('list_id', models.DateTimeField(default=django.utils.timezone.now)),
                ('company_id', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_profile', models.TextField(blank=True)),
                ('company_product', models.TextField(blank=True, null=True)),
                ('user_note', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='result_list',
            name='create_date',
        ),
    ]
