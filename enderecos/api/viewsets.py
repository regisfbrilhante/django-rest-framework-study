from rest_framework import viewsets
from enderecos.models import Enderecos
from .serializers import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecoSerializer