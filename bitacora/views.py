from django.shortcuts import render

from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated

from monedas.models import EquipajeExtra, DetalleValoresMonetarios
from transporte.models import transporte
from viajeros.models import Viajero
from .models import bitacora


class TransportesSerializer(serializers.Serializer):
    class Meta:
        model = transporte
        fields = "__all__"


class DetallesValoresSerializer(serializers.Serializer):
    class Meta:
        model = DetalleValoresMonetarios
        fields = "__all__"


class ViajeroSerializer(serializers.Serializer):
    class Meta:
        model = Viajero
        fields = "__all__"


class EquipajeSerializer(serializers.Serializer):
    class Meta:
        model = EquipajeExtra
        fields = "__all__"


class BitacoraSerializer(serializers.Serializer):
    viajero = ViajeroSerializer(many=False)
    equipajes_extra = EquipajeSerializer(many=True)
    detallesValoresMonetarios = DetallesValoresSerializer(many=True)
    transporte = TransportesSerializer(many=False)

    class Meta:
        model = bitacora
        fields = "__all__"


class BitacoraViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = bitacora.objects.all()
    serializer_class = BitacoraSerializer
    permission_classes = [IsAuthenticated]
