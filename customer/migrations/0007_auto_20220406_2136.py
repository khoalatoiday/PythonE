# Generated by Django 2.2 on 2022-04-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
