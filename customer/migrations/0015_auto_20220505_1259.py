# Generated by Django 2.2 on 2022-05-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_auto_20220505_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
