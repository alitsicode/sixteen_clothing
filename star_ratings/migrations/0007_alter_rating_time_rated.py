# Generated by Django 4.0.5 on 2022-08-19 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('star_ratings', '0006_alter_rating_time_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='time_rated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
