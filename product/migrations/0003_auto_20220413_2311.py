# Generated by Django 2.2 on 2022-04-13 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0002_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.CreateModel(
            name='OrderedBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('bookId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Book')),
                ('cartId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Cart')),
            ],
        ),
    ]
