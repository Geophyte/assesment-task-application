from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from ..models import Comment, Task, Category
import json

User = get_user_model()


class CommentViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category', created_by=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test description', completed=False, category=self.category)
        self.comment = Comment.objects.create(task=self.task, user=self.user, text='Test comment')
        self.client = Client()
        self.client.force_login(self.user)

    def test_create_comment(self):
        data = {'task': self.task.pk, 'text': 'Test comment'}
        response = self.client.post('/comments/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.count(), 2)

    def test_retrieve_comment(self):
        response = self.client.get(f'/comments/{self.comment.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['text'], 'Test comment')

    def test_update_comment(self):
        data = {'task': self.task.pk, 'text': 'Updated comment'}
        response = self.client.put(f'/comments/{self.comment.pk}/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.get(pk=self.comment.pk).text, 'Updated comment')

    def test_partial_update_comment(self):
        data = {'text': 'New comment'}
        response = self.client.patch(f'/comments/{self.comment.pk}/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.get(pk=self.comment.pk).text, 'New comment')

    def test_delete_comment(self):
        response = self.client.delete(f'/comments/{self.comment.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Comment.objects.count(), 0)

    # Test custom actions

    def test_user_comments(self):
        response = self.client.get(f'/comments/user/{self.user.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_task_comments(self):
        response = self.client.get(f'/comments/task/{self.task.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_user_task_comments(self):
        response = self.client.get(f'/comments/user/{self.user.pk}/task/{self.task.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
