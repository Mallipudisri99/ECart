# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2023-06-18 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
