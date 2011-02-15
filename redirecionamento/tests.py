from django.test import TestCase
from django.test.client import Client
from redirecionamento.models import Endereco

class RedirecionamentoTest(TestCase):
    def setUp(self):
        Endereco(codigo = 'google', destino = 'http://www.google.com/').save()
    
    def test_adicionar(self):
        resposta = self.client.post('/', {'codigo': 'google', 'destino': 'http://www.google.com/'})
        self.assertEquals(resposta.status_code, 200)
        self.assertEquals(resposta.content, '{"codigo": "google", "destino": "http://www.google.com/"}')
        self.assertEquals(Endereco.objects.get(codigo = 'google').destino, 'http://www.google.com/')
    
    def test_adicionar_mesmo_codigo(self):
        resposta = self.client.post('/', {'codigo': 'google', 'destino': 'http://www.google.com.br/'})
        self.assertEquals(resposta.status_code, 200)
        self.assertEquals(resposta.content, '{"erro": true}')
        self.assertEquals(Endereco.objects.get(codigo = 'google').destino, 'http://www.google.com/')
    
    def test_adicionar_mesmo_destino(self):
        resposta = self.client.post('/', {'codigo': 'busca', 'destino': 'http://www.google.com/'})
        self.assertEquals(resposta.status_code, 200)
        self.assertEquals(resposta.content, '{"codigo": "google", "destino": "http://www.google.com/"}')
        self.assertEquals(Endereco.objects.get(codigo = 'google').destino, 'http://www.google.com/')
        self.assertRaises(Endereco.DoesNotExist, Endereco.objects.get, codigo = 'busca')
    
    def test_ir(self):
        resposta = self.client.get('/google')
        self.assertRedirects(resposta, 'http://www.google.com/', status_code = 301)
    
    def test_ir_inexistente(self):
        resposta = self.client.get('/busca')
        self.assertEquals(resposta.status_code, 404)
