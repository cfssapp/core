# Generated by Django 3.0.3 on 2021-01-14 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0003_auto_20210113_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owneritem', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]