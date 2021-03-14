from django.urls import path
from rest_framework import routers

from common.views import TipoCambioView

urlpatterns = [
    path('tipo-cambio/', TipoCambioView.as_view()),
]