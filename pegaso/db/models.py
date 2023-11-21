from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    # TODO: Create User relationship
    saram = models.CharField(unique=True,
                             max_length=8,
                             verbose_name="SARAM")
    cpf = models.CharField(unique=True,
                           max_length=14,
                           verbose_name="CPF")
    # TODO: Validate CPF and SARAM inputs
    full_name = models.CharField(max_length=100, verbose_name="Nome Completo")
    op_name = models.CharField(max_length=50, verbose_name="Nome de Guerra")
    telephone = models.CharField(max_length=20, verbose_name="Telefone (WhatsApp)",
                                 blank=True, null=True)

    # Rank options
    TEN_BRIG = "TB"
    MAJ_BRIG = "MB"
    BRIG = "BR"
    CORONEL = "CL"
    TEN_CORONEL = "TC"
    MAJOR = "MJ"
    CAPITAO = "CP"
    TEN_1 = "1T"
    TEN_2 = "2T"
    ASPIRANTE = "AP"
    SUBOFICIAL = "SO"
    SGT_1 = "1S"
    SGT_2 = "2S"
    SGT_3 = "3S"

    RANK_CHOICES = [
        (TEN_BRIG, "Tenente-Brigadeiro"),
        (MAJ_BRIG, "Major-Brigadeiro"),
        (BRIG, "Brigadeiro"),
        (CORONEL, "Coronel"),
        (TEN_CORONEL, "Tenente-Coronel"),
        (MAJOR, "Major"),
        (CAPITAO, "Capitão"),
        (TEN_1, "Primeiro-Tenente"),
        (TEN_2, "Segundo-Tenente"),
        (ASPIRANTE, "Aspirante"),
        (SUBOFICIAL, "Sub-Oficial"),
        (SGT_1, "Primeiro-Sargento"),
        (SGT_2, "Segundo-Sargento"),
        (SGT_3, "Terceiro-Sargento")
    ]

    rank = models.CharField(max_length=2,
                            choices=RANK_CHOICES,
                            verbose_name="Posto / Graduação")

    # Operational
    # TODO: Add qualification per project

    def __str__(self):
        return "{} {}".format(self.rank, self.op_name)

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
