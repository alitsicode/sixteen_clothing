# Generated by Django 4.0.5 on 2022-08-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_rename_hits_filter_hitsfilter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('empty', 'empty'), ('have', 'have'), ('in_order', 'in_order')], default='have', max_length=8),
        ),
    ]