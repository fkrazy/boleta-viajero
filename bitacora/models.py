
from django.db import models

from paises.models import Pais


class bitacora (models.Model):
    accion = models.CharField(max_length=8, default="")
    fecha = models.DateField()
    motivo_viaje = models.CharField(max_length=20, default="")
    #id_aduana = models.ForeignKey(aduanas, on_delete=models.CASCADE)
    #id_viajero = models.ForeignKey(viajeros, on_delete=models.CASCADE)
    #id_destino = models.ForeignKey(destinos, on_delete=models.CASCADE)
    #id_transporte = models.ForeignKey(transportes, on_delete=models.CASCADE)
    pais_procedencia = models.ForeignKey(Pais, verbose_name='pais', related_name="paises", on_delete=models.PROTECT)
    numero_familiares = models.IntegerField()
    cantidad_equipaje = models.IntegerField()
    cantidad_no_acompanado = models.IntegerField()
    dinero_mayor_diezmil = models.FloatField()
    #id_moneda = models.ForeignKey(detalle_valores_monetarios, on_delete=models.CASCADE)
    #id_material = models.ForeignKey(detalle_valors_monetarios, on_delete=models.CASCADE)
    animales_plantas_alimentos = models.FloatField()
    producto_quimico_sustancias = models.FloatField()
    mercancias_distintas = models.FloatField()
    exoneraciones_tributos = models.FloatField()