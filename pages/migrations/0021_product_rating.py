# Generated by Django 4.0.5 on 2022-08-20 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.STAR_RATINGS_RATING_MODEL),
        ('pages', '0020_remove_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.ManyToManyField(related_name='rating', to=settings.STAR_RATINGS_RATING_MODEL),
        ),
    ]
