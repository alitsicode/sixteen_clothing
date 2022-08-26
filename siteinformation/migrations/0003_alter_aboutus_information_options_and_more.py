# Generated by Django 4.0.5 on 2022-08-09 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('siteinformation', '0002_aboutus_information'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus_information',
            options={'verbose_name': 'aboutus_information'},
        ),
        migrations.AlterModelOptions(
            name='contactmessage',
            options={'verbose_name': 'contactmessage'},
        ),
        migrations.AlterField(
            model_name='aboutus_information',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='aboutus_information',
            name='work_description',
            field=models.TextField(verbose_name='work_description'),
        ),
        migrations.AlterField(
            model_name='aboutus_information',
            name='work_image',
            field=models.ImageField(upload_to='work_image', verbose_name='work_image'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='body',
            field=models.TextField(verbose_name='your text'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='date_time_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_time_create'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='subject'),
        ),
    ]