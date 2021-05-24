from django.urls import path

from viajeros.views import ViajerosFrecuentesView, ViajerosRepublicaView, Viajeros10kView

urlpatterns = [
    path('reporte/frecuentes/', ViajerosFrecuentesView.as_view()),
    path('reporte/republica/', ViajerosRepublicaView.as_view()),
    path('reporte/relacion10k/', Viajeros10kView.as_view()),
]