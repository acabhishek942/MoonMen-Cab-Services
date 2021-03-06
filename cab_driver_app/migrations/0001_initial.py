# Generated by Django 2.0.9 on 2018-10-30 20:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=15)),
                ('manufacture_year', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=15)),
                ('colour', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CabDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('driving_license_number', models.CharField(max_length=20, unique=True)),
                ('expiry_date', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('rating', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('deaf', models.BooleanField(default=False)),
                ('total_rides', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_start_time', models.DateTimeField()),
                ('shift_end_time', models.DateTimeField(null=True)),
                ('ongoing', models.BooleanField(default=True)),
                ('rides_completed', models.IntegerField(default=0)),
                ('cab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cab_driver_app.Cab')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cab_driver_app.CabDriver')),
            ],
        ),
        migrations.AddField(
            model_name='cab',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cab_driver_app.CabDriver'),
        ),
    ]
