# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-03 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('konfera', '0017_order_processing_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receipt_of', to='konfera.Order'),
        ),
    ]
