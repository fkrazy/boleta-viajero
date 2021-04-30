from django.db import models


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=30, default="")
    nombre_nacionalidad = models.CharField(max_length=25, default="")
    abreviatura = models.CharField(max_length=5, default="")


class Aduana(models.Model):
    clasificacion = models.CharField(max_length=15)
    nombre = models.CharField(max_length=80)
    pais = models.ForeignKey(Pais, verbose_name='pais', related_name="aduanas", on_delete=models.PROTECT)
