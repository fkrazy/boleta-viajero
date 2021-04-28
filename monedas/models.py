from django.db import models


class Moneda(models.Model):
    moneda = models.CharField(max_length=20)


class MaterialPrecioso(models.Model):
    titulo = models.CharField(max_length=30)
    clase = models.CharField(max_length=20)


class DetalleValoresMonetarios(models.Model):
    valor_dolares = models.DecimalField(decimal_places=2, max_digits=9)
    origen_fondos = models.TextField(max_length=255)
    destino_fondos = models.TextField(max_length=255)

    moneda = models.ForeignKey(Moneda, verbose_name='moneda', related_name="monedas", on_delete=models.PROTECT)
    material = models.ForeignKey(MaterialPrecioso, verbose_name='material', related_name="materiales",
                                 on_delete=models.PROTECT)


class EquipajeExtra(models.Model):
    cantidad = models.IntegerField()
    descripcion = models.TextField(max_length=255)
    valor_dolares= models.DecimalField(decimal_places=2, max_digits=9)
