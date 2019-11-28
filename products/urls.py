from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet, UserProductList, \
    UserProductByDateList

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('userProducts/date/<str:date>/', UserProductByDateList.as_view()),
    path('userProducts/', UserProductList.as_view()),
    path('', include(router.urls))
]
