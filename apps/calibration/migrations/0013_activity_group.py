# Generated by Django 3.0.3 on 2021-09-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibration', '0012_remove_activity_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='group',
            field=models.CharField(default=1, max_length=255),
        ),
    ]