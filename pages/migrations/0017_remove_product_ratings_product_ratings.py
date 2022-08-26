# Generated by Django 4.0.5 on 2022-08-19 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.STAR_RATINGS_RATING_MODEL),
        ('pages', '0016_product_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ratings',
        ),
        migrations.AddField(
            model_name='product',
            name='ratings',
            field=models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.STAR_RATINGS_RATING_MODEL),
        ),
    ]
