# Generated by Django 3.2.4 on 2021-07-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_auto_20180628_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelsubscription',
            name='client_ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
