from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password',)

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        if self.validate_data.get("password"):
            instance.set_password(self.validated_data['password'])
        return instance
