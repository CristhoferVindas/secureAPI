from rest_framework.test import APITestCase
from rest_framework import status

class UserAPITestCase(APITestCase):
    def test_create_user(self):
        data = {"name": "John Doe", "email": "johndoe@example.com", "password": "securepassword123"}
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_protected_view_without_token(self):
        response = self.client.get('/api/protected/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_view_with_token(self):
        user_data = {"name": "John Doe", "email": "johndoe@example.com", "password": "securepassword123"}
        self.client.post('/api/register/', user_data)

        response = self.client.post('/api/token/', {
            'email': 'johndoe@example.com',
            'password': 'securepassword123',
        })
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get('/api/protected/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
