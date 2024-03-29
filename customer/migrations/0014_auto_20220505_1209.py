# Generated by Django 2.2 on 2022-05-05 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_auto_20220413_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fullName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.FullName'),
        ),
    ]
