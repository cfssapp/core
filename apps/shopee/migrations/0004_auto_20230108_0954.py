# Generated by Django 3.0.3 on 2023-01-08 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopee', '0003_auto_20230108_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='list',
        ),
        migrations.AddField(
            model_name='cart',
            name='list',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopee.Product'),
        ),
    ]
