from django.db import models


class transporte(models.Model):
    tipo = models.CharField(max_length=15, default="")
    nombre = models.CharField(max_length=15, default="")
    numero = models.IntegerField()
    matricula = models.CharField(max_length=10, default="")
    nombre_empresa = models.CharField(max_length=50, default="")
