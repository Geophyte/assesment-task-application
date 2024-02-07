from rest_framework import viewsets
from ..models import UserProfile
from ..serializers.user_profile import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
