# Generated by Django 2.2 on 2022-05-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20220502_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedbook',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='orderedbook',
            name='totalPrice',
            field=models.FloatField(blank=True),
        ),
    ]
