# Generated by Django 4.0.5 on 2022-08-25 06:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0023_bookmark'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bookmark',
            new_name='bookmarks',
        ),
    ]
