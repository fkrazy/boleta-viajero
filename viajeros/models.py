from django.db import models
from paises.models import Pais


class Viajero (models.Model):
    numero_documento = models.IntegerField()
    tipo_documento = models.CharField(max_length=10, default="")
    primer_nombre = models.CharField(max_length=45, default="")
    segundo_nombre = models.CharField(max_length=45, default="")
    tercer_nombre = models.CharField(max_length=45, default="")
    primer_apellido = models.CharField(max_length=35, default="")
    segundo_apellido = models.CharField(max_length=35, default="")
    tercer_apellido = models.CharField(max_length=35, default="")
    nacionalidad = models.ForeignKey(Pais, verbose_name='nacionalidad', related_name="nacionalidades",
                                     on_delete=models.PROTECT)
    sexo = models.CharField(max_length=10, default="")
    fecha_nacimiento = models.DateField()
    pais_residencia = models.ForeignKey(Pais, verbose_name='residencia', related_name="residencias",
                                        on_delete=models.PROTECT)
