# Generated by Django 4.0.5 on 2022-08-12 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customeuser_avatar_alter_customeuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='avatar',
            field=models.ImageField(upload_to='user_avatar', verbose_name='avatar'),
        ),
    ]