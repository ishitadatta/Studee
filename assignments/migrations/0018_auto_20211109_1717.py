# Generated by Django 2.2.5 on 2021-11-09 11:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0017_auto_20211109_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 11, 47, 39, 835698, tzinfo=utc)),
        ),
    ]
