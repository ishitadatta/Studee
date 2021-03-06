# Generated by Django 2.2.5 on 2021-11-13 09:09

from django.db import migrations, models
import django_resized.forms
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bio',
            field=tinymce.models.HTMLField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=100, size=[50, 80], upload_to='authentication/profile_photos'),
        ),
    ]
