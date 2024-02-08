from rest_framework import serializers
from .models import Programa

class ProgramaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Programa.

    Este serializer converte objetos Programa em representações JSON e vice-versa.
    """
    class Meta:
        model = Programa
        fields = ['titulo', 'tipo', 'data_lancamento', 'likes']
