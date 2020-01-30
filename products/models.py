from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    carbohydrates = models.IntegerField()
    proteins = models.IntegerField()
    fats = models.IntegerField()

    def __str__(self):
        return self.name


class UserProduct(models.Model):
    mealtime_choices = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Supper', 'Supper')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mealtime = models.CharField(max_length=10, choices=mealtime_choices)
    date = models.DateField()
    weight = models.IntegerField()

    class Meta:
        unique_together = ('product', 'date', 'mealtime')
