# Generated by Django 3.1.4 on 2021-11-09 04:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0013_auto_20211108_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 4, 2, 9, 794121, tzinfo=utc)),
        ),
    ]
