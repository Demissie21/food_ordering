from django import template

register = template.Library()

@register.filter
def calc_total_price(cart_items):
    total = 0
    for item in cart_items:
        total += item.food.price * item.quantity
    return "%.2f" % total
