from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    calories = models.IntegerField()
    carbohydrates = models.IntegerField()
    proteins = models.IntegerField()
    fats = models.IntegerField()
