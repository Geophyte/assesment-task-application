from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from ..models import CustomUser

User = get_user_model()


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register(self):
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post('/register/', data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(CustomUser.objects.filter(username='newuser').exists())

    def test_login_user(self):
        user = User.objects.create_user(username='testuser', password='password')
        data = {'username': 'testuser', 'password': 'password'}
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_whoami(self):
        user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(user)
        response = self.client.get('/whoami/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')
