# Generated by Django 2.2.5 on 2021-11-18 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20211116_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='course_credits',
        ),
    ]
