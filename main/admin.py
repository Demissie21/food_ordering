from django.contrib import admin
from .models import Food, CartItem, Order

admin.site.register(Food)
admin.site.register(CartItem)
admin.site.register(Order)

