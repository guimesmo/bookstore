from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password',)

