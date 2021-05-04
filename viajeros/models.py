from django.db import models
from paises.models import Pais


class Viajero (models.Model):
    email = models.EmailField(null=True)
    numero_documento = models.CharField(max_length=45, default="")
    tipo_documento = models.CharField(max_length=10, default="")
    primer_nombre = models.CharField(max_length=45, default="")
    segundo_nombre = models.CharField(max_length=45, default="")
    tercer_nombre = models.CharField(max_length=45, default="", null=True, blank=True)
    primer_apellido = models.CharField(max_length=35, default="")
    segundo_apellido = models.CharField(max_length=35, default="")
    tercer_apellido = models.CharField(max_length=35, default="", null=True, blank=True)
    nacionalidad = models.ForeignKey(Pais, verbose_name='nacionalidad', related_name="nacionalidades",
                                     on_delete=models.PROTECT)
    sexo = models.CharField(max_length=10, default="")
    fecha_nacimiento = models.DateField()
    pais_residencia = models.ForeignKey(Pais, verbose_name='residencia', related_name="residencias",
                                        on_delete=models.PROTECT)
