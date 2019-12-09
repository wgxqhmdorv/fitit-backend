from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)
    password = serializers.CharField()

    def validate(self, data):
        if data["confirmPassword"] != data["password"]:
            raise serializers.ValidationError("Passwords don't match")
        return data

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirmPassword']
