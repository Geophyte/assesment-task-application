from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from ..models import CustomUser, Category, Task, Comment
from ..serializers.comment import CommentSerializer

User = get_user_model()


class CommentSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category', created_by=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test description', category=self.category, created_by=self.user)
        self.comment_data = {
            'task': self.task.pk,
            'text': 'Test comment'
        }
        self.factory = RequestFactory()
        self.request = self.factory.post('/fake-url/')
        self.request.user = self.user

    def test_comment_serializer_create(self):
        serializer = CommentSerializer(data=self.comment_data, context={'request': self.request})
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Comment.objects.count(), 1)