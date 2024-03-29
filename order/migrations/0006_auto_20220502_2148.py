# Generated by Django 2.2 on 2022-05-02 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20220502_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='customerId',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customerId',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='paymentId',
            new_name='payment',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='shipmentId',
            new_name='shipment',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='amount',
        ),
    ]
