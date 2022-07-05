# Generated by Django 3.2.9 on 2022-04-26 10:19

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_userprofileinfo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boat_name', models.CharField(blank=True, max_length=254)),
                ('boat_type', models.CharField(blank=True, choices=[('Wooden', 'Wooden'), ('Fiber', 'Fiber'), ('Aluminium', 'Aluminiun'), ('Steel', 'Steel'), ('Others', 'Others')], default=None, max_length=255)),
                ('arrival', models.DateField()),
                ('departure', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=254)),
                ('last_name', models.CharField(blank=True, max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Jetty_Bathymetry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathymetry', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Jetty_Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='jetty')),
            ],
        ),
        migrations.CreateModel(
            name='Jetty_Supervisors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=254)),
                ('surname', models.CharField(blank=True, max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Jetty_Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Ridership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_departure', models.CharField(choices=[('Arrival', 'Arrival'), ('Departure', 'Departure')], default=None, max_length=254)),
                ('arrival_departure_time', models.DateTimeField()),
                ('number_of_passengers', models.IntegerField()),
                ('transport_fare', models.PositiveIntegerField(blank=True)),
                ('waterguard', models.CharField(blank=True, max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='DepthA',
        ),
        migrations.DeleteModel(
            name='DepthB',
        ),
        migrations.DeleteModel(
            name='DepthC',
        ),
        migrations.DeleteModel(
            name='DepthD',
        ),
        migrations.AddField(
            model_name='jetty',
            name='boat_type',
            field=models.CharField(blank=True, choices=[('Wooden', 'Wooden'), ('Fiber', 'Fiber'), ('Aluminium', 'Aluminiun'), ('Steel', 'Steel'), ('Others', 'Others')], default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='jetty',
            name='number_of_boats',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ridership',
            name='arrival_departure_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivalOrDepartureLocation', to='api.jetty'),
        ),
        migrations.AddField(
            model_name='ridership',
            name='boat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.boat'),
        ),
        migrations.AddField(
            model_name='ridership',
            name='jetty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ridershipLocation', to='api.jetty'),
        ),
        migrations.AddField(
            model_name='jetty_videos',
            name='jetty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jetty'),
        ),
        migrations.AddField(
            model_name='jetty_supervisors',
            name='jetty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jetty'),
        ),
        migrations.AddField(
            model_name='jetty_pictures',
            name='jetty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jetty'),
        ),
        migrations.AddField(
            model_name='jetty_bathymetry',
            name='jetty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jetty'),
        ),
        migrations.AddField(
            model_name='boat',
            name='boat_driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.drivers'),
        ),
    ]
