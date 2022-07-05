# Generated by Django 3.2.9 on 2022-05-09 09:33

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20220509_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='jetty',
            name='picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, size=[250, 150], upload_to='small_jetty'),
        ),
    ]