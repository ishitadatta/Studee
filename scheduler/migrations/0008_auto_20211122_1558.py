# Generated by Django 2.2.5 on 2021-11-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20211121_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
