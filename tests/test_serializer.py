from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):
  def setUp(self):
    self.populando_banco_de_dados_para_teste()

    # Passando uma instância do modelo (Programa) para o serializer 
    self.serializer = ProgramaSerializer(instance=self.programa)
  
  def test_verifica_campos_serializados(self):
    """Teste para verificar os campos que estão sendo serializados"""
    data = self.serializer.data
    self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))
  
  def test_verifica_conteudo_dos_campos_serializados(self):
    """Teste que verifica o conteúdo dos campos serializados"""
    data = self.serializer.data
    self.assertEqual(data['titulo'], self.programa.titulo)
    self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
    self.assertEqual(data['tipo'], self.programa.tipo)
    self.assertEqual(data['likes'], self.programa.likes)

  def populando_banco_de_dados_para_teste(self):
    """Criando uma instância no banco de dados para ser usado nos métodos de teste"""
    self.programa = Programa(
      titulo = 'Título teste',
      data_lancamento = '2023-02-21',
      tipo = 'F',
      likes = 1,
      dislikes = 2
    )