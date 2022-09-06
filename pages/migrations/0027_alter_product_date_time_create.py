# Generated by Django 4.0.5 on 2022-09-05 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_alter_product_date_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_time_create',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created'),
        ),
    ]
