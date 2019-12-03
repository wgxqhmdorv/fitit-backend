from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField()

    def validate(self, data):
        if data["confirm_password"] != data["password"]:
            raise serializers.ValidationError("Passwords don't match")
        return data

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']
