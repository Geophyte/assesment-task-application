from rest_framework import viewsets
from ..models import Task
from ..serializers.task import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
