from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Comment
from ..serializers.comment import CommentSerializer
from ..permissions import IsOwnerOrReadOnly, IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=['get'])
    def user_comments(self, request, user_id=None):
        queryset = self.get_queryset().filter(user_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def task_comments(self, request, task_id=None):
        queryset = self.get_queryset().filter(task_id=task_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def user_task_comments(self, request, user_id=None, task_id=None):
        queryset = self.get_queryset().filter(user_id=user_id, task_id=task_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
