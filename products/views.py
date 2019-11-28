from rest_framework import viewsets, generics
from rest_framework.response import Response

from products.models import Product, UserProduct
from products.serializers import ProductSerializer, UserProductSerializer, \
    UserProductWithProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserProductList(generics.ListCreateAPIView):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer

    def get(self, request, *args, **kwargs):
        products = UserProduct.objects.all().select_related()
        serializer = UserProductWithProductSerializer(products, many=True)
        return Response(serializer.data)


class UserProductByDateList(generics.ListAPIView):
    serializer_class = UserProductWithProductSerializer

    def get_queryset(self):
        date = self.kwargs['date']
        queryset = UserProduct.objects.filter(date=date)
        return queryset
