# Generated by Django 3.0.3 on 2021-01-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0009_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]