# Generated by Django 3.0.3 on 2021-01-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0011_foodorder_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]