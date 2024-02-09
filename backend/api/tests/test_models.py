from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import CustomUser, Category, Task, Comment

User = get_user_model()


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category', created_by=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test description', category=self.category, created_by=self.user)

    def test_custom_user_creation(self):
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get(username='testuser').username, 'testuser')

    def test_category_creation(self):
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get(name='Test Category').name, 'Test Category')
        self.assertEqual(Category.objects.get(name='Test Category').created_by, self.user)

    def test_task_creation(self):
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get(title='Test Task').title, 'Test Task')
        self.assertEqual(Task.objects.get(title='Test Task').category, self.category)
        self.assertEqual(Task.objects.get(title='Test Task').created_by, self.user)

    def test_comment_creation(self):
        comment = Comment.objects.create(task=self.task, user=self.user, text='Test comment')
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get(pk=comment.pk).text, 'Test comment')
