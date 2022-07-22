from django.db import models

# Create your models here.

class Empleado(models.Model):
    idempleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length= 60)
    puesto = models.CharField(max_length= 50)
    area = models.CharField(max_length= 80)

class Mobiliario(models.Model):
    noinventario = models.IntegerField()
    tipo = models.CharField(max_length=30)
    noserie = models.IntegerField(primary_key=True)
    valor = models.IntegerField()
