# Generated by Django 3.1.4 on 2021-11-08 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0009_auto_20211108_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 8, 14, 8, 7, 220230, tzinfo=utc)),
        ),
    ]
