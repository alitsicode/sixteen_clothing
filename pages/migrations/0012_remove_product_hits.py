# Generated by Django 4.0.5 on 2022-08-16 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_ipaddress_delete_comment_product_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='hits',
        ),
    ]
