# Generated by Django 3.0.9 on 2020-08-20 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0018_activityparticipant_reminder_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='weight_for_average',
            field=models.FloatField(null=True),
        ),
    ]