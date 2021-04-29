from django.db import models
from bitacora.models import bitacora


class Moneda(models.Model):
    moneda = models.CharField(max_length=20)


class MaterialPrecioso(models.Model):
    titulo = models.CharField(max_length=30)
    clase = models.CharField(max_length=20)


class DetalleValoresMonetarios(models.Model):
    valor_dolares = models.DecimalField(decimal_places=2, max_digits=9)
    origen_fondos = models.TextField(max_length=255)
    destino_fondos = models.TextField(max_length=255)
    bitacora = models.ForeignKey(bitacora, verbose_name='bitacora', related_name="detallesValoresMonetarios",
                                 on_delete=models.PROTECT, null=True)
    moneda = models.ForeignKey(Moneda, verbose_name='moneda', related_name="monedas", on_delete=models.PROTECT)
    material = models.ForeignKey(MaterialPrecioso, verbose_name='material', related_name="materiales",
                                 on_delete=models.PROTECT)


class EquipajeExtra(models.Model):
    cantidad = models.IntegerField()
    descripcion = models.TextField(max_length=255)
    valor_dolares= models.DecimalField(decimal_places=2, max_digits=9)
    bitacora = models.ForeignKey(bitacora, verbose_name='bitacora', related_name="equipajes_extra",
                                 on_delete=models.PROTECT, null=True)
