from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='john_doe', email='john_doe@example.com')
        user.set_password('john_pass')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='john_doe')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'john_doe',
            'email': 'john_doe@example.com',
            'password': 'john_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password2'][0], 'This field is required.')

    def test_register_user_api(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'john_doe',
            'email': 'john_doe@example.com',
            'password': 'john_password',
            'password2': 'john_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token_len = len(response.data.get('token', 0))
        self.assertGreater(token_len, 0)

    def test_login_user_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'john_doe',
            'password': 'john_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', 0)
        token_len = 0
        if token != 0:
            token_len = token
        self.assertGreater(token_len, 0)

    def test_login_user_api_fail(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'john_doe',
            'password': 'john_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # 400
        token = response.data.get("token", 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertEqual(token_len, 0)

    def test_token_login_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'john_doe',
            'password': 'john_password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 400
        token = response.data.get("token", None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)

    def test_token_register_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'john_doe',
            'password': 'john_pass',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 400
        token = response.data.get("token", None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        url2 = api_reverse('api-auth:register')
        data2 = {
            'username': 'john_doe',
            'email': 'john_doe@example.com',
            'password': 'john_pass',
            'password2': 'john_pass'
        }
        response = self.client.post(url2, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # 403
