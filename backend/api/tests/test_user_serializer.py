from django.test import TestCase
from ..models import CustomUser
from ..serializers.user import UserSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password',
            'profile_picture': None
        }

    def test_user_serializer_create(self):
        serializer = UserSerializer(data=self.user_data)
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_user_serializer_update(self):
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='password')
        updated_user_data = {
            'username': 'updateduser',
            'email': 'updated@example.com',
            'password': 'newpassword',
            'profile_picture': None
        }
        serializer = UserSerializer(instance=user, data=updated_user_data)
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        user.refresh_from_db()
        self.assertEqual(user.username, 'updateduser')
        self.assertEqual(user.email, 'updated@example.com')
