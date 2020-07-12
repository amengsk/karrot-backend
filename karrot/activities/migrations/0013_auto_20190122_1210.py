# Generated by Django 2.1.5 on 2019-01-22 12:10

from django.db import migrations
import karrot.activities.models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0012_rename_date_range_to_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=karrot.activities.models.CustomDateTimeRangeField(default=karrot.activities.models.default_activity_date_range),
        ),
    ]