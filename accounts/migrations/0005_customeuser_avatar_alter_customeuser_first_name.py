# Generated by Django 4.0.5 on 2022-08-11 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customeuser_email_alter_customeuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='avatar',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='user_avatar'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customeuser',
            name='first_name',
            field=models.CharField(default='firstname', max_length=200),
        ),
    ]
