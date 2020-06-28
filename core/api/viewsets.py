from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):

    # Criando filtragem em get_queryset
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        # return super().get_queryset()
        return PontoTuristico.objects.filter(aprovado=True)
    
    
