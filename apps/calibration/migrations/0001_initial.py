# Generated by Django 3.0.3 on 2021-08-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_id', models.CharField(default='not set', max_length=100)),
                ('instrument', models.CharField(default='not set', max_length=100)),
                ('customer', models.CharField(default='not set', max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
