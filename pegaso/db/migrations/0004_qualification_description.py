# Generated by Django 4.2.7 on 2023-11-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_project_max_flight_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='description',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
