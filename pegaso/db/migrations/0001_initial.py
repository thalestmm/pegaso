# Generated by Django 4.2.7 on 2023-11-21 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=5)),
                ('number', models.IntegerField()),
                ('cruise_speed', models.IntegerField()),
                ('basic_weight', models.IntegerField()),
                ('max_tof_weight', models.IntegerField()),
                ('max_ldg_weight', models.IntegerField()),
                ('burn_rate', models.IntegerField()),
                ('max_passengers', models.IntegerField()),
                ('max_flight_time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
            ],
        ),
    ]
