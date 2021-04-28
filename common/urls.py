from django.urls import path
from rest_framework import routers

from common.views import TipoCambioView, GetGroups

urlpatterns = [
    path('tipo-cambio/', TipoCambioView.as_view()),
    path('groups/', GetGroups.as_view()),
]