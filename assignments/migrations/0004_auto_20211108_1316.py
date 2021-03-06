# Generated by Django 2.2.5 on 2021-11-08 07:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0003_auto_20211107_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher_details',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 8, 7, 46, 2, 843437, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='duration',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='marks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
