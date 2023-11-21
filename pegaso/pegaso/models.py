from django.db import models
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
    type = models.CharField(max_length=5)
    number = models.IntegerField(max_length=4)

    # Performance data
    cruise_speed = models.IntegerField()
    basic_weight = models.IntegerField()  # TODO: Define standard  unit
    max_tof_weight = models.IntegerField()  # Takeoff
    max_ldg_weight = models.IntegerField()  # Landing
    burn_rate = models.IntegerField()  # TODO: Define standard unit
    max_passengers = models.IntegerField()
    max_flight_time = models.FloatField()


class Qualification(models.Model):
    name = models.CharField(max_length=2)


class User(AbstractUser):
    pass
