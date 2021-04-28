from django.contrib import admin

# Register your models here.
from transporte.models import transporte, empresa_transporte

admin.site.register(transporte)
admin.site.register(empresa_transporte)
