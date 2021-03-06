# Generated by Django 3.2.9 on 2022-05-19 08:56

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_jetty_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jetty_pictures',
            name='small_picture',
        ),
        migrations.AlterField(
            model_name='jetty',
            name='picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[250, 150], upload_to='small_jetty'),
        ),
        migrations.AlterField(
            model_name='jetty_pictures',
            name='medium_picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[500, 300], upload_to='medium_jetty'),
        ),
        migrations.AlterField(
            model_name='jetty_pictures',
            name='picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[1920, 1080], upload_to='jetty'),
        ),
    ]
