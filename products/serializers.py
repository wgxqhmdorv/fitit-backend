from rest_framework import serializers

from products.models import Product, UserProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        exclude = []


class UserProductWithProductSerializer(UserProductSerializer):
    product = ProductSerializer()

    # class Meta(UserProductSerializer.Meta):
    #     exclude = ['user']
