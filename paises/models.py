from django.db import models


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=30, default="")
    nombre_nacionalidad = models.CharField(max_length=25, default="")
    abreviatura = models.CharField(max_length=5, default="")
