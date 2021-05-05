from django.urls import path

from viajeros.views import ViajerosFrecuentesView

urlpatterns = [
    path('reporte/frecuentes/', ViajerosFrecuentesView.as_view()),
]