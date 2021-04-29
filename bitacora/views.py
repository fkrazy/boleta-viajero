from django.shortcuts import render

from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from .models import bitacora


class BitacoraSerializer(serializers.Serializer):
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
