# Generated by Django 2.2 on 2022-05-07 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_auto_20220505_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fullName',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.FullName'),
        ),
    ]
