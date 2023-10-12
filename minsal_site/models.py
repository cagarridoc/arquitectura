from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30)
class hospital(models.Model):
    nombre_hospital = models.PositiveBigIntegerField()
class Muerte(models.Model):
    fechaMuerte = models.DateField()
    causaMuerte = models.CharField(max_length=300)
class paciente(models.Model):
    nombrePaciente = models.CharField(max_length=50)
    sNombrePaciente = models.CharField(max_length=50)
    apPaterno = models.CharField(max_length=50)
    apMaterno = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()
    fechaMuerte = models.DateField()
    generoPaciente = models.CharField(max_length=1)
    fecNacPaciente = models.DateField()
class condicionSocial(models.Model):
    tipoCondicionSocial = models.CharField(max_length=50)