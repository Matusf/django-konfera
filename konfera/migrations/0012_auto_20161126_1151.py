# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('konfera', '0011_auto_20161121_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('name', models.CharField(max_length=255)),
                ('text_template', models.TextField()),
                ('html_template', models.TextField()),
                ('counter', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
