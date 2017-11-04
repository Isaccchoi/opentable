from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=11)
    join = models.DateField(auto_now_add=True)
    head_chef = models.CharField(max_length=50)
    description = models.TextField()
    food_kind = models.CharField(max_length=15)
    average_price = models.PositiveIntegerField(max_length=8)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField(max_length=9)
    image = models.ImageField()
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return f'{self.restaurant.name} - {self.name}'


class ImageForRestaurant(models.Model):
    image = models.ImageField()
    restaurant = models.ForeignKey(Restaurant)
    