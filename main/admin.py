from django.contrib import admin
from .models import Food, Order, CartItem

admin.site.register(Food)
admin.site.register(Order)
admin.site.register(CartItem)
