from django.db import models


class empresa_transporte(models.Model):
    nombre_empresa = models.CharField(max_length=50, default="")


class transporte(models.Model):
    empresa = models.ForeignKey(empresa_transporte, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=15, default="")
    nombre = models.CharField(max_length=15, default="")
    numero = models.IntegerField()
    matricula = models.CharField(max_length=10, default="")
