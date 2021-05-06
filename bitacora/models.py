
from django.db import models

from paises.models import Pais, Aduana
from transporte.models import transporte
from viajeros.models import Viajero


class bitacora (models.Model):
    objects = None
    CREADO = 1
    VALIDADO = 2
    TERMINADO = 3
    ESTADOS = (
        (CREADO, "Creado"),
        (VALIDADO, "Validado"),
        (TERMINADO, "Terminado")
    )
    accion = models.SmallIntegerField(choices=ESTADOS, default=CREADO)
    fecha = models.DateField()
    motivo_viaje = models.CharField(max_length=20, default="")
    aduana = models.ForeignKey(Aduana, on_delete=models.CASCADE, null=True)
    viajero = models.ForeignKey(Viajero, related_name="bitacoras", on_delete=models.CASCADE, null=True)
    transporte = models.ForeignKey(transporte, on_delete=models.CASCADE, null=True)
    pais_procedencia = models.ForeignKey(Pais, verbose_name='pais', related_name="paises_bitacora",
                                         on_delete=models.PROTECT)
    pais_destino = models.ForeignKey(Pais, verbose_name='pais', related_name="paises_destino", null=True,
                                     on_delete=models.PROTECT)
    direccion = models.CharField(max_length=70, default="")
    numero_familiares = models.IntegerField()
    cantidad_equipaje = models.IntegerField()
    cantidad_no_acompanado = models.IntegerField()
    dinero_mayor_diezmil = models.BooleanField()
    animales_plantas_alimentos = models.BooleanField()
    producto_quimico_sustancias = models.BooleanField()
    mercancias_distintas = models.BooleanField()
    exoneraciones_tributos = models.BooleanField()
