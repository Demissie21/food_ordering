from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Order, CartItem
from django.contrib.auth.decorators import login_required

# Display the menu
def menu(request):
    items = Food.objects.filter(available=True)
    return render(request, 'main/menu.html', {'items': items})

# Handle placing an order
@login_required
def place_order(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('items')

        if not selected_items:
            return render(request, 'main/place_order.html', {
                'items': Food.objects.filter(available=True),
                'error': 'Please select at least one item.'
            })

        # Create the order for the logged-in user
        order = Order.objects.create(user=request.user)

        # Add selected food items as CartItems linked to this order
        for item_id in selected_items:
            food = get_object_or_404(Food, id=item_id)
            cart_item = CartItem.objects.create(user=request.user, food=food, quantity=1)
            order.items.add(cart_item)

        return redirect('menu')  # Redirect after successful order

    else:
        items = Food.objects.filter(available=True)
        return render(request, 'main/place_order.html', {'items': items})
