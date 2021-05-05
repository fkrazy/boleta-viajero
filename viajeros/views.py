from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from viajeros.models import Viajero


class ViajeroFrecuenteSerializer(serializers.ModelSerializer):
    viajes = serializers.SerializerMethodField()

    def get_viajes(self, obj):
        return obj.bitacoras.count()

    class Meta:
        model = Viajero
        fields = ["numero_documento", "viajes"]


class ViajerosFrecuentesView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        serializer = ViajeroFrecuenteSerializer(Viajero.objects.all(), many=True)
        return Response(serializer.data)

