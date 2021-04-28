from django.contrib import admin

# Register your models here.
from monedas.models import Moneda, MaterialPrecioso, DetalleValoresMonetarios, EquipajeExtra

admin.site.register(Moneda)
admin.site.register(MaterialPrecioso)
admin.site.register(DetalleValoresMonetarios)
admin.site.register(EquipajeExtra)
