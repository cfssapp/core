# Generated by Django 3.0.3 on 2021-09-11 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calibration', '0008_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calibration.Certificate'),
        ),
    ]
