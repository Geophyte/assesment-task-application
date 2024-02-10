from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from ..models import Category, Task
from ..serializers.task import TaskSerializer

User = get_user_model()


class TaskSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category', created_by=self.user)
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test description',
            'category': self.category.pk
        }
        self.factory = RequestFactory()
        self.request = self.factory.post('/fake-url/')
        self.request.user = self.user

    def test_task_serializer_create(self):
        serializer = TaskSerializer(data=self.task_data, context={'request': self.request})
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Task.objects.count(), 1)

    def test_task_serializer_update(self):
        task = Task.objects.create(title='Old Task', description='Old description', category=self.category, created_by=self.user)
        updated_task_data = {
            'title': 'Updated Task',
            'description': 'Updated description',
            'category': self.category.pk
        }
        serializer = TaskSerializer(instance=task, data=updated_task_data, context={'request': self.request})
        self.assertTrue(serializer.is_valid())
        serializer.save()
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task')
        self.assertEqual(task.description, 'Updated description')
