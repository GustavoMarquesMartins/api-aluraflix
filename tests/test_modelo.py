from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

  def setUp(self):
    """Método executado antes de cada teste para configurar o ambinete"""
    self.populando_banco_de_dados_para_teste()
  
  def test_verifica_atributos_do_programa(self):
    """Teste que verifica atributos do programa com valores default"""
    self.assertEquals(self.programa.titulo, 'Título teste')
    self.assertEquals(self.programa.tipo, 'F')
    self.assertEquals(self.programa.data_lancamento, '2023-04-20')
    self.assertEquals(self.programa.likes, 0)
    self.assertEquals(self.programa.dislikes, 0)
  
  def populando_banco_de_dados_para_teste(self):
    """Criando uma instância no banco de dados para ser usado nos métodos de teste"""
    self.programa = Programa(
      titulo = 'Título teste',
      data_lancamento = '2023-04-20'
    )