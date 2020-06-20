# Generated by Django 3.0.2 on 2020-06-15 12:21
from datetime import datetime

from django.db import migrations
from pytz import utc


def migrate(apps, schema_editor):
    ConversationMeta = apps.get_model('conversations', 'ConversationMeta')

    min_date = datetime.min.replace(tzinfo=utc)

    for meta in ConversationMeta.objects.filter(conversations_marked_at__isnull=True):
        meta.conversations_marked_at = min_date
        meta.save()

    for meta in ConversationMeta.objects.filter(threads_marked_at__isnull=True):
        meta.threads_marked_at = min_date
        meta.save()


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0036_add_conversation_meta'),
    ]

    operations = [
        migrations.RunPython(migrate, migrations.RunPython.noop, elidable=True),
    ]