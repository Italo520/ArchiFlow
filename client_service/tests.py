from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Client

User = get_user_model()

class ClientViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.client_data = {
            'name': 'Test Client',
            'email': 'test@example.com',
            'phone': '1234567890',
            'address': '123 Test Street'
        }
        self.client_instance = Client.objects.create(**self.client_data)

    def test_create_client(self):
        url = reverse('client-list')
        data = {
            'name': 'New Client',
            'email': 'new@example.com',
            'phone': '0987654321',
            'address': '456 New Avenue'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_clients(self):
        url = reverse('client-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_instance.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_instance.pk})
        data = {
            'name': 'Updated Client',
            'email': 'updated@example.com',
            'phone': '1112223333',
            'address': '789 Updated Road'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_instance.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)