# Generated by Django 2.2 on 2022-05-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_fullname_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fullname',
            name='avatar',
        ),
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]
