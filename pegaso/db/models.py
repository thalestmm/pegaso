from django.db import models
from django.conf import settings
from datetime import datetime, timedelta


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )
    saram = models.CharField(unique=True, max_length=8, verbose_name="SARAM")
    cpf = models.CharField(unique=True, max_length=14, verbose_name="CPF")
    # TODO: Validate CPF and SARAM inputs
    full_name = models.CharField(max_length=100, verbose_name="Nome Completo")
    op_name = models.CharField(max_length=50, verbose_name="Nome de Guerra")
    telephone = models.CharField(max_length=20, verbose_name="Telefone (WhatsApp)", blank=True, null=True)

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

    rank = models.CharField(max_length=2, choices=RANK_CHOICES, verbose_name="Posto / Graduação")

    # Operational
    # TODO: Add qualification per project

    def __str__(self):
        return "{} {}".format(self.rank, self.op_name)


class OperatorProfile(models.Model):
    # Specialty levels
    PIL_IN = "IN"
    PIL_OPR = "PO"
    PIL_BAS = "PB"
    PIL_AL = "AL"
    MC_IN = "IC"
    MC_OPR = "MC"
    MC_AL = "AC"
    COM_IN = "IF"
    COM_OPR = "TF"
    COM_AL = "AF"

    SPECIALTY_CHOICES = [
        (PIL_IN, "Piloto Instrutor"),
        (PIL_OPR, "Piloto Operacional"),
        (PIL_BAS, "Piloto Básico"),
        (PIL_AL, "Piloto-Aluno"),
        (MC_IN, "Mecânico Instrutor"),
        (MC_OPR, "Mecânico Operacional"),
        (MC_AL, "Mecânico-Aluno"),
        (COM_IN, "Comissário Instrutor"),
        (COM_OPR, "Comissário Operacional"),
        (COM_AL, "Comissário-Aluno")
    ]

    specialty = models.CharField(max_length=2, choices=SPECIALTY_CHOICES, verbose_name="Operacionalidade")
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, verbose_name="Projeto", null=True)
    last_flight_date = models.DateField(verbose_name="Data do último voo", default=datetime.today())
    yearly_hours = models.DurationField(verbose_name="Horas voadas no ano")

    # TODO: Days since last flight and script to reset all yearly hours (confirm action etc)

    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} {}".format(self.user, self.specialty, self.project)

    def save(self, *args, **kwargs):
        self.days_since_last_flight = (datetime.today().date() - self.last_flight_date).days

        instructor_classes = [self.PIL_IN, self.MC_IN, self.COM_IN]
        operational_classes = [self.PIL_OPR, self.PIL_BAS, self.MC_OPR, self.COM_OPR]

        self.is_adapted = True

        # Instrutores desadaptam com mais de 45 dias e operacionais com mais de 35. Alunos não desadaptam.

        if self.specialty in operational_classes and self.days_since_last_flight > 35:
            self.is_adapted = False
        if self.specialty in instructor_classes and self.days_since_last_flight > 45:
            self.is_adapted = False

        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=10, verbose_name="Tipo de Aeronave")

    def __str__(self):
        return self.name


class Airplane(models.Model):
    type = models.ForeignKey("Project", on_delete=models.CASCADE, verbose_name="Tipo de Aeronave")
    number = models.IntegerField(unique=True, primary_key=True, verbose_name="Matrícula")

    # Performance data
    cruise_speed = models.IntegerField(verbose_name="Velocidade de Cruzeiro (kt)")
    basic_weight = models.IntegerField(verbose_name="Peso Básico Operacional")  # TODO: Define standard  unit
    max_tof_weight = models.IntegerField(verbose_name="Peso Máximo DEP")  # Takeoff
    max_ldg_weight = models.IntegerField(verbose_name="Peso Máximo PSO")  # Landing
    burn_rate = models.IntegerField(verbose_name="Consumo de Combustível")  # TODO: Define standard unit
    max_passengers = models.IntegerField(verbose_name="Número máximo de PAX") # TODO: Será que é necessário manter?
    max_flight_time = models.TimeField(verbose_name="Autonomia")

    def __str__(self):
        return "{} {}".format(self.type, self.number)


class Airport(models.Model):
    icao = models.CharField(max_length=4, verbose_name="Código ICAO")
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cidade")

    latitude = models.FloatField()
    longitude = models.FloatField()

    has_fueling = models.BooleanField(default=False, verbose_name="Abastecimento (CELOG)")

    def __str__(self):
        return self.icao
