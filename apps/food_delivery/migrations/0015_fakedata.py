# Generated by Django 3.0.3 on 2021-01-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0014_auto_20210129_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalesData', models.ManyToManyField(to='food_delivery.SalesData')),
            ],
        ),
    ]
