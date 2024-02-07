from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):

  # Carregando a fixture (programas_iniciais)
  fixtures = ['programas_iniciais']

  def test_que_verifica_carregamento_das_fixtures(self):
    """Verifica carregamento da fixture para o banco de dados de teste"""
    programa = Programa.objects.get(pk=1) 
    todos_os_programas = Programa.objects.all()
    self.assertEqual(programa.titulo, 'Coisas bizarras')
    self.assertEqual(len(todos_os_programas), 9)