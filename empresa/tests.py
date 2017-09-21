import unittest
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Rota

class APITest(TestCase):

  def test_client_list(self):
    response = self.client.get(reverse('viagens-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_funcionario_list(self):
    response = self.client.get(reverse('funcionario-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
