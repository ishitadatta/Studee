# Generated by Django 2.2.5 on 2021-11-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0028_auto_20211113_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='name',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='university_id',
        ),
    ]
