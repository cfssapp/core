# Generated by Django 3.0.3 on 2021-01-20 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='upload_pics'),
        ),
    ]
