from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from ..models import Task, Category
import json

User = get_user_model()


class TaskViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category', created_by=self.user)
        self.client = Client()
        self.client.force_login(self.user)

    def test_create_task(self):
        data = {'title': 'Test Task', 'description': 'Test description', 'completed': False, 'category': self.category.pk}
        response = self.client.post('/tasks/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_retrieve_task(self):
        task = Task.objects.create(title='Test Task', description='Test description', completed=False, category=self.category)
        response = self.client.get(f'/tasks/{task.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        task = Task.objects.create(title='Test Task', description='Test description', completed=False, category=self.category)
        data = {'title': 'Updated Task', 'description': 'Updated description', 'completed': True, 'category': self.category.pk}
        response = self.client.put(f'/tasks/{task.pk}/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.get().title, 'Updated Task')
        self.assertEqual(Task.objects.get().description, 'Updated description')
        self.assertTrue(Task.objects.get().completed)

    def test_partial_update_task(self):
        task = Task.objects.create(title='Test Task', description='Test description', completed=False, category=self.category)
        data = {'title': 'New Title'}
        response = self.client.patch(f'/tasks/{task.pk}/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.get().title, 'New Title')

    def test_delete_task(self):
        task = Task.objects.create(title='Test Task', description='Test description', completed=False, category=self.category)
        response = self.client.delete(f'/tasks/{task.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.count(), 0)

    # Test permissions
    def test_task_create_permission(self):
        unauthorized_client = Client()
        response = unauthorized_client.post('/tasks/', {'title': 'Test Task', 'description': 'Test description'})
        self.assertEqual(response.status_code, 403)

    def test_task_update_permission(self):
        task = Task.objects.create(title='Test Task', description='Test description', completed=False, category=self.category)
        unauthorized_client = Client()
        response = unauthorized_client.put(f'/tasks/{task.pk}/', {'title': 'Updated Task'})
        self.assertEqual(response.status_code, 403)
