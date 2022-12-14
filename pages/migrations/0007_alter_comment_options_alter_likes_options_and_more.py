# Generated by Django 4.0.5 on 2022-08-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_comment_comment_text_alter_comment_is_suggest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'comment'},
        ),
        migrations.AlterModelOptions(
            name='likes',
            options={'verbose_name': 'likes'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_suggest',
            field=models.BooleanField(default=True, verbose_name='suggest it?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.CharField(default='d', max_length=1),
        ),
    ]
