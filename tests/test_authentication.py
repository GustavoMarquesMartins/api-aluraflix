from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AuthenticationUserTestCase(APITestCase):

  def setUp(self):
    self.populando_banco_de_dados_para_teste()
  
  def test_autenticacao_user_com_credencias_corretas(self):
    """Verifica se um usuário com crendencias corretas conseque se autenticar"""
    user = authenticate(username='c3po', password='123456')
    self.assertTrue((user is not None) and user.is_authenticated)

  def populando_banco_de_dados_para_teste(self):
    """Criando uma instância no banco de dados para ser usado nos métodos de teste"""
    self.user = User.objects.create_user(username="c3po", password='123456')