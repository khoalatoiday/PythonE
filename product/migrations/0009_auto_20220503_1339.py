# Generated by Django 2.2 on 2022-05-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20220502_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderedbook',
            name='totalPrice',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
