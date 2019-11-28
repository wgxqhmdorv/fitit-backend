from collections import defaultdict

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

    def list(self, request, *args, **kwargs):
        products = self.get_queryset()
        serialized_products = self.serializer_class(products, many=True).data

        products_by_mealtime = defaultdict(list)

        for product in serialized_products:
            del product['date']
            mealtime = product.pop('mealtime')
            products_by_mealtime[mealtime].append(product)

        return Response(products_by_mealtime)
