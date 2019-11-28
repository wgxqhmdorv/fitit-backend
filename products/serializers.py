from rest_framework import serializers

from products.models import Product, UserProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'calories', 'carbohydrates', 'proteins', 'fats']


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ['id', 'user', 'product', 'mealtime', 'date', 'weight']
