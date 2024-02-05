from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):

  def setUp(self):
    self.populando_banco_de_dados_para_teste()
    self.serializer = ProgramaSerializer(instance=self.programa)
  
  def test_verifica_campos_serializados(self):
    """Teste para verificar os campos que estão sendo serializados"""
    data = self.serializer.data
    self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

  def populando_banco_de_dados_para_teste(self):
    self.programa = Programa(
      titulo = 'Título teste',
      data_lancamento = '2023-02-21',
      tipo = 'F',
      likes = 1,
      dislikes = 2
    )