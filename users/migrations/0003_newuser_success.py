# Generated by Django 3.0.3 on 2021-08-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210813_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='success',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]