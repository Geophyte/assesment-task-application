from rest_framework import viewsets
from ..models import Category
from ..serializers.category import CategorySerializer
from ..permissions import IsAuthenticated, NoModify


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, NoModify]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
