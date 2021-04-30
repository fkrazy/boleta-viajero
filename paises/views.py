from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from paises.models import Pais, Aduana


class PaisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = "__all__"


class PaisesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Pais.objects.all()
    serializer_class = PaisesSerializer
    permission_classes = [IsAuthenticated]


class AduanasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aduana
        fields = "__all__"


class AduanasViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Aduana.objects.all()
    serializer_class = AduanasSerializer
    permission_classes = [IsAuthenticated]


class RepublicasViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Pais.objects.filter(aduanas__isnull=False)
    serializer_class = PaisesSerializer
    permission_classes = [IsAuthenticated]
