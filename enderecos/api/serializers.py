from rest_framework import serializers
from enderecos.models import Enderecos

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ['id', 'linha1', 'linha2', 'cidade', 'estado','pais', 'longitude','latitude']
