from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from ..models import Category
from ..serializers.category import CategorySerializer

User = get_user_model()


class CategorySerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category_data = {
            'name': 'Test Category',
        }
        self.factory = RequestFactory()
        self.request = self.factory.post('/fake-url/')
        self.request.user = self.user

    def test_category_serializer_create(self):
        serializer = CategorySerializer(data=self.category_data, context={'request': self.request})
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.get(name='Test Category')
        self.assertEqual(category.created_by, self.user)
