from rest_framework import serializers
from ..models import Comment
from .user_profile import UserSerializer
from .task import TaskSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    task = TaskSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
