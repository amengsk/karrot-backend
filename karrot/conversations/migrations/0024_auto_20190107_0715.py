# Generated by Django 2.1.5 on 2019-01-07 07:15

from django.db import migrations
from django.db.models import F, Case, When


def convert_email_notification_setting(apps, schema_editor):
    ConversationParticipant = apps.get_model('conversations', 'ConversationParticipant')
    ConversationParticipant.objects.all().update(
        muted=Case(
            When(email_notifications=False, then=True),
            default=False,
        )
    )


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('conversations', '0023_conversationparticipant_muted'),
    ]

    operations = [migrations.RunPython(convert_email_notification_setting, migrations.RunPython.noop, elidable=True)]