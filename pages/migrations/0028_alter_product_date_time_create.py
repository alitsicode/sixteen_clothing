# Generated by Django 4.0.5 on 2022-09-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_alter_product_date_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_created'),
        ),
    ]
