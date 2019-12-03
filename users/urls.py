from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from users.views import UserList, TokenBlacklist

urlpatterns = [
    path('', UserList.as_view()),
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist_token/', TokenBlacklist.as_view(), name="token_blacklist")
]
