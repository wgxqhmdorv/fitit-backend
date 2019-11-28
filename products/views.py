from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, UserProduct
from products.serializers import ProductSerializer, UserProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserProductList(APIView):

    def get(self, request):
        user_products = UserProduct.objects.all()
        # serializer = UserProductSerializer(user_products, many=True)
        product = Product.objects.get(id=1)
        print(product)
        print(user_products.get('id'))
        # print(serializer.data)
        # return Response(serializer.data)
