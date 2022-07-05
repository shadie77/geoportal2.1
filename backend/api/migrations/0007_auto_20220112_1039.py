# Generated by Django 3.2.9 on 2022-01-12 09:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_boundary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water_Boundary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='Boundary',
        ),
    ]
