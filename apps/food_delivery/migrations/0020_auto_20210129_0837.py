# Generated by Django 3.0.3 on 2021-01-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0019_delete_fakedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='y',
            field=models.IntegerField(default=100, max_length=100),
        ),
    ]
