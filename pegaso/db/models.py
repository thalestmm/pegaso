from django.db import models
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
    type = models.CharField(max_length=5)
    number = models.IntegerField()

    # Performance data
    cruise_speed = models.IntegerField()
    basic_weight = models.IntegerField()  # TODO: Define standard  unit
    max_tof_weight = models.IntegerField()  # Takeoff
    max_ldg_weight = models.IntegerField()  # Landing
    burn_rate = models.IntegerField()  # TODO: Define standard unit
    max_passengers = models.IntegerField()
    max_flight_time = models.TimeField()

    def __str__(self):
        return "{} {}".format(self.type, self.number)


class Qualification(models.Model):
    name = models.CharField(max_length=2)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Airport(models.Model):
    icao = models.CharField(max_length=4)
    city = models.CharField(max_length=100, null=True, blank=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    has_fueling = models.BooleanField(default=False)

    def __str__(self):
        return self.icao
