from django.urls import path

from common.views import TipoCambioView, GetGroups, MonedasBanguatView, TipoCambioMonedaView

urlpatterns = [
    path('tipo-cambio/', TipoCambioView.as_view()),
    path('monedas_banguat/', MonedasBanguatView.as_view()),
    path('tipo_cambio_moneda/<int:id>', TipoCambioMonedaView.as_view()),
    path('groups/', GetGroups.as_view()),
]