from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from monedas.models import Moneda, MaterialPrecioso


class MaterialSerializer(serializers.Serializer):
    class Meta:
        model = MaterialPrecioso
        fields = "__all__"


class MaterialViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = MaterialPrecioso.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]


class MonedaSerializer(serializers.Serializer):
    class Meta:
        model = Moneda
        fields = "__all__"


class MonedasViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer
    permission_classes = [IsAuthenticated]
