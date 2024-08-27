# Generated by Django 5.0.6 on 2024-07-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='battery_capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='processor',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ram_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='speed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
