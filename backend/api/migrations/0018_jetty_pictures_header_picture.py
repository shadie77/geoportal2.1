# Generated by Django 3.2.9 on 2022-05-24 16:12

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20220519_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='jetty_pictures',
            name='header_picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[1050, 300], upload_to='header_jetty'),
        ),
    ]
