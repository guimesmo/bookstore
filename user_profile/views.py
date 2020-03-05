from django.contrib.auth import get_user_model
from rest_framework import viewsets


from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = get_user_model().objects.all()
