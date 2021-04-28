from django.contrib import admin

# Register your models here.
from paises.models import Pais, Aduana

admin.site.register(Pais)
admin.site.register(Aduana)
