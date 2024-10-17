from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='category')
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='subcategories')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    in_stock = models.BooleanField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    discount = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    choices = [
        ('NEW', 'New'),
        ('POPULAR', 'Popular'),
        ('DISCOUNT', 'Discount'),
    ]
    status = models.CharField(max_length=100, choices=choices)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    choices = [
        ('PENDING', 'Pending'),
        ('DELIVERED', 'Delivered'),
        ('CANCELED', 'Canceled'),
    ]
    status = models.CharField(max_length=100, choices=choices)

    def __str__(self):
        return self.user


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_order = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.order

