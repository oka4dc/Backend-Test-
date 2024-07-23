from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AccountTests(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_data = {
            'email': 'okaforchikelue93@gmail.com',
            'password': 'testpassword',
            'first_name': 'Dennis',
            'last_name': 'Okafor'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.user.set_password(self.user_data['password'])
        self.user.save()

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # One user is created in setUp and one by this test
        self.assertEqual(User.objects.get(id=2).email, self.user_data['email'])

    def test_login_user(self):
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_logout_user(self):
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        login_response = self.client.post(self.login_url, login_data, format='json')
        refresh_token = login_response.data['refresh']
        response = self.client.post(self.logout_url, {'refresh': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

