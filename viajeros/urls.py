from django.urls import path

from viajeros.views import ViajerosFrecuentesView, ViajerosRepublicaView

urlpatterns = [
    path('reporte/frecuentes/', ViajerosFrecuentesView.as_view()),
    path('reporte/republica/', ViajerosRepublicaView.as_view()),
]