# Generated by Django 3.0.3 on 2021-02-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobb', '0004_auto_20210210_2045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='post',
            name='topic_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
