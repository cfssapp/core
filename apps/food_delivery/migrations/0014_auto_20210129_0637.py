# Generated by Django 3.0.3 on 2021-01-29 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0013_csv'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(default='not set', max_length=100)),
                ('y', models.CharField(default='not set', max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='fooditem',
            options={'ordering': ['id']},
        ),
    ]
