from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

  def setUp(self):
    # obtendo todos os endpoints do recurso programas
    self.lista_url = reverse('programas-list')

    self.populando_banco_de_dados_para_teste()
  
  def test_autenticacao_user_com_credencias_corretas(self):
    """Verifica se um usuário com crendencias corretas conseque se autenticar"""
    user = authenticate(username='c3po', password='123456')
    self.assertTrue((user is not None) and user.is_authenticated)
  
  def test_requisicao_get_nao_autorizada(self):
    """Teste que verifica uma requisição GET de um usuário não autorizado """
    resposta = self.client.get(self.lista_url)
    self.assertEqual(resposta.status_code, status.HTTP_401_UNAUTHORIZED)
  
  def test_autenticacao_user_com_username_incorreto(self):
    """Teste que verifica autenticação de um user com username incorreto"""
    user = authenticate(username='c3poo', password='123456')
    self.assertFalse((user is not None) and user.is_authenticated)

  def test_autenticacao_user_com_password_incorreto(self):
    """Teste que verifica autenticação de um user com password incorreto"""
    user = authenticate(username='c3po', password='1234566')
    self.assertFalse((user is not None) and user.is_authenticated) 

  def test_requisicao_get_com_user_autenticado(self):
    """Teste que verifica uma requisição GET para um usuário autenticado"""
    self.client.force_authenticate(self.user)
    resposta = self.client.get(self.lista_url)
    self.assertEqual(resposta.status_code, status.HTTP_200_OK)

  def populando_banco_de_dados_para_teste(self):
    """Criando uma instância no banco de dados para ser usado nos métodos de teste"""
    self.user = User.objects.create_user(username="c3po", password='123456')