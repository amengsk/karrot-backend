# Generated by Django 2.2.6 on 2019-10-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickups', '0015_auto_20190129_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickupdate',
            name='feedback_as_sum',
            field=models.BooleanField(default=False),
        ),
    ]
