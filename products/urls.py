from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet, UserProductList

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('userProducts/', UserProductList.as_view()),
    path('', include(router.urls))
]
