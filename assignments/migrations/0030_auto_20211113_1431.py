# Generated by Django 2.2.5 on 2021-11-13 09:01

import assignments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0029_auto_20211113_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=assignments.models.get_filename),
        ),
    ]
