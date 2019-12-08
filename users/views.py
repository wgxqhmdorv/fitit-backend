from django.db.migrations import serializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.data)
            return Response("Account created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# TODO Flush blacklisted tokens with `flushexpiredtokens` every few days
class TokenBlacklist(APIView):
    def post(self, request):
        token = request.data.pop("token")
        refresh_token = RefreshToken(token)
        refresh_token.blacklist()
        return Response({"code": "token_blacklisted"})
