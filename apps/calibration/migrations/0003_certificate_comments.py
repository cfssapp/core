# Generated by Django 3.0.3 on 2021-08-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibration', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='comments',
            field=models.ManyToManyField(blank=True, to='calibration.Comment'),
        ),
    ]
