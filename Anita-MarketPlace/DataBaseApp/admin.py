from django.contrib import admin
from .models import *

admin.site.register([Category, Brand, Product, Order, OrderItem])