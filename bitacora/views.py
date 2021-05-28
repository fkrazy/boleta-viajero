from io import BytesIO

import qrcode
from django.core.mail import EmailMessage
from django.db import transaction

from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from monedas.models import EquipajeExtra, DetalleValoresMonetarios
from transporte.models import transporte
from viajeros.models import Viajero
from .models import bitacora


class TransportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = transporte
        fields = "__all__"


class DetallesValoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleValoresMonetarios
        fields = "__all__"


class ViajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viajero
        fields = "__all__"


class EquipajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipajeExtra
        fields = "__all__"


class BitacoraSerializer(serializers.ModelSerializer):
    viajero = ViajeroSerializer(many=False)
    equipajes_extra = EquipajeSerializer(many=True)
    detallesValoresMonetarios = DetallesValoresSerializer(many=True)
    transporte = TransportesSerializer(many=False)

    class Meta:
        model = bitacora
        fields = "__all__"


# serializers para api mostrar datos formulario viajero
class TransportesDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = transporte
        fields = "__all__"


class DetallesValoresDetalleSerializer(serializers.ModelSerializer):
    # slugrelatedfield de moneda y material
    moneda = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='moneda'
    )

    material = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='titulo'
    )

    class Meta:
        model = DetalleValoresMonetarios
        fields = "__all__"


class ViajeroDetalleSerializer(serializers.ModelSerializer):
    # slugrelatedfield de nacionalidad y pais residencia
    nacionalidad = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre_nacionalidad'
    )

    pais_residencia = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre_pais'
    )

    class Meta:
        model = Viajero
        fields = "__all__"


class EquipajeDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipajeExtra
        fields = "__all__"


class BitacoraDetalleSerializer(serializers.ModelSerializer):
    viajero = ViajeroDetalleSerializer(many=False)
    equipajes_extra = EquipajeDetalleSerializer(many=True)
    detallesValoresMonetarios = DetallesValoresDetalleSerializer(many=True)
    transporte = TransportesDetalleSerializer(many=False)

    # slugrelatedfield de pais procedencia, pais destino y aduana
    pais_procedencia = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre_pais'
    )

    pais_destino = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre_pais'
    )

    aduana = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre'
    )

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

    @action(detail=True, methods=["post"])
    def validate(self, request, pk=None):
        bitacora_obj = self.get_object()
        if bitacora_obj.accion == bitacora_obj.CREADO:
            bitacora_obj.accion = bitacora_obj.VALIDADO
            qr = qrcode.QRCode()
            qr.make(f"{bitacora_obj.viajero.numero_documento},{bitacora_obj.fecha}")
            qr = qr.make_image()
            email = EmailMessage(
                'Boleta Validada',
                'Se adjunta la imagen qr para que puedan validar la boleta en ventanilla',
                'frankuniversidad12@gmail.com',
                [bitacora_obj.viajero.email],
            )
            stream = BytesIO()
            qr.save(stream, format="png")
            stream.seek(0)
            imgObj = stream.read()
            email.attach('boleta.png', imgObj, 'image/png')
            email.send()
            bitacora_obj.save()
            return Response({'status': 'validado'})
        else:
            return Response({'status': 'bitacora en estado incorrecto'})

    @action(detail=True, methods=["get"])
    def detalle(self, request, pk=None):
        bitacora = self.get_object()
        serializer = BitacoraDetalleSerializer(bitacora)
        return Response(serializer.data)

    @transaction.atomic
    def perform_create(self, serializer):
        viajero_obj = serializer.validated_data.pop('viajero')
        viajero_obj = set_viajero_detail_as_index(viajero_obj)
        viajero = Viajero.objects.filter(numero_documento=viajero_obj.get("numero_documento")).first()
        if viajero:
            viajero.save()
        else:
            viajero_serializer = ViajeroSerializer(data=viajero_obj)
            viajero_serializer.is_valid(raise_exception=True)
            viajero = viajero_serializer.save()
        equipajes_extra = serializer.validated_data.pop('equipajes_extra', None)
        detalles_valores_monetarios = serializer.validated_data.pop('detallesValoresMonetarios', None)
        transporte = serializer.validated_data.pop('transporte')
        bitacora = serializer.save()
        bitacora.viajero_id = viajero.id
        equipajes_extra_serializer = EquipajeSerializer(data=equipajes_extra, many=True)
        equipajes_extra_serializer.is_valid(raise_exception=True)
        equipajes = equipajes_extra_serializer.save()
        bitacora.equipajes_extra.set(equipajes)
        detalles_valores_monetarios = list(map(set_valores_detail_as_index, detalles_valores_monetarios))
        detalles_valores_monetarios_serializer = DetallesValoresSerializer(data=detalles_valores_monetarios, many=True)
        detalles_valores_monetarios_serializer.is_valid(raise_exception=True)
        valores = detalles_valores_monetarios_serializer.save()
        bitacora.detallesValoresMonetarios.set(valores)
        transportes_serializer = TransportesSerializer(data=transporte)
        transportes_serializer.is_valid(raise_exception=True)
        transporte = transportes_serializer.save()
        bitacora.transporte_id = transporte.id

    @action(detail=False, methods=["get"])
    def ventanilla(self, request, pk=None):
        obj_bitacora = self.get_queryset().filter(Viajero__numero_documento=self.kwargs.get('doc'),
                                                  fecha=self.kwargs.get('fecha'))
        serializer = ObtenerFormularioQRSerializer(obj_bitacora)
        return Response(serializer.data)


def set_valores_detail_as_index(val):
    val["moneda"] = val["moneda"].id
    val["material"] = val["material"].id
    return val


def set_viajero_detail_as_index(val):
    val["nacionalidad"] = val["nacionalidad"].id
    val["pais_residencia"] = val["pais_residencia"].id
    return val


class DatosViajeroQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viajero
        fields = ('numero_documento', 'primer_nombre', 'segundo_nombre', 'tercer_nombre', 'primer_apellido',
                  'segundo_apellido', 'tercer_apellido')


class ObtenerFormularioQRSerializer(serializers.ModelSerializer):
    viajero = DatosViajeroQRSerializer(many=False)
    class Meta:
        model = bitacora
        fields = ('viajero', 'get_accion_display')
