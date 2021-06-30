from rest_framework import serializers
from core.models import PuntoReciclag


class CompletePuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoReciclag
        fields = '__all__'


class PublicPuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoReciclag
        exclude = ('id_usuario','ruta_imagen')
