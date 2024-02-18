from django.contrib import admin

from .models import Products, Order, OrderItem

admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)