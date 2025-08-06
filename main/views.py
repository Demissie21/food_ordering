from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem, Order

def menu(request):
    items = FoodItem.objects.filter(available=True)
    return render(request, 'main/menu.html', {'items': items})

def place_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        selected_items = request.POST.getlist('items')

        if not name or not selected_items:
            return render(request, 'main/place_order.html', {
                'items': FoodItem.objects.filter(available=True),
                'error': 'Please enter your name and select at least one item.'
            })

        total = 0
        food_items = []
        for item_id in selected_items:
            item = get_object_or_404(FoodItem, id=item_id)
            food_items.append(item)
            total += item.price

        order = Order.objects.create(customer_name=name, total_price=total)
        order.items.set(food_items)
        return redirect('menu')  # or 'order_success' if you want a confirmation page

    else:
        items = FoodItem.objects.filter(available=True)
        return render(request, 'main/place_order.html', {'items': items})
