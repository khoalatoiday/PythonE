# Generated by Django 2.2 on 2022-04-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phoneNumber',
            field=models.CharField(max_length=11, null=True),
        ),
    ]