# Generated by Django 3.0.3 on 2021-09-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calibration', '0010_auto_20210911_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='certificate_id2',
        ),
    ]
