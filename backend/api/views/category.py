from rest_framework import viewsets
from ..models import Category
from ..serializers.category import CategorySerializer
from ..permissions import IsOwnerOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
