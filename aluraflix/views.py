from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import ProgramaSerializer
from .models import Programa


class ProgramaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manipulação de Programas.
    """
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

    # Configuração dos filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['tipo']
    search_fields = ['titulo']

    # Configuração da autenticação e permissão
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]