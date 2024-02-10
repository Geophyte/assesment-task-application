from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from ..models import Category

User = get_user_model()


class CategoryViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.force_login(self.user)

    def test_create_category(self):
        data = {'name': 'Test Category'}
        response = self.client.post('/categories/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Test Category')

    def test_retrieve_category(self):
        category = Category.objects.create(name='Test Category')
        response = self.client.get(f'/categories/{category.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Category')

    def test_update_category(self):
        category = Category.objects.create(name='Test Category')
        data = {'name': 'Updated Category'}
        response = self.client.put(f'/categories/{category.pk}/', data)
        self.assertEqual(response.status_code, 403)

    def test_partial_update_category(self):
        category = Category.objects.create(name='Test Category')
        data = {'name': 'New Category Name'}
        response = self.client.patch(f'/categories/{category.pk}/', data)
        self.assertEqual(response.status_code, 403)

    def test_delete_category(self):
        category = Category.objects.create(name='Test Category')
        response = self.client.delete(f'/categories/{category.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Category.objects.count(), 0)

    # Test permissions
    def test_category_create_permission(self):
        unauthorized_client = APIClient()
        response = unauthorized_client.post('/categories/', {'name': 'Test Category'})
        self.assertEqual(response.status_code, 403)

    def test_category_update_permission(self):
        category = Category.objects.create(name='Test Category')
        unauthorized_client = APIClient()
        response = unauthorized_client.put(f'/categories/{category.pk}/', {'name': 'Updated Category'})
        self.assertEqual(response.status_code, 403)
