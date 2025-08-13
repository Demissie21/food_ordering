from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Order, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'main/order_history.html', {'orders': orders})

@login_required
def order_success(request):
    return render(request, 'main/order_success.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in after registering
            messages.success(request, '✅ Registration successful!')
            return redirect('menu')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def menu(request):
    items = Food.objects.filter(available=True)
    return render(request, 'main/menu.html', {'items': items})

@login_required
def place_order(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('items')
        if not selected_items:
            messages.error(request, '⚠️ Please select at least one item to order.')
            items = Food.objects.filter(available=True)
            return render(request, 'main/place_order.html', {'items': items})

        order = Order.objects.create(user=request.user)
        for item_id in selected_items:
            food = get_object_or_404(Food, id=item_id)
            quantity = int(request.POST.get(f'quantity_{item_id}', 1))
            cart_item = CartItem.objects.create(user=request.user, food=food, quantity=quantity)
            order.items.add(cart_item)

        messages.success(request, '✅ Your order has been placed successfully!')
        return redirect('order_confirmation', order_id=order.id)

    items = Food.objects.filter(available=True)
    return render(request, 'main/place_order.html', {'items': items})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'main/order_confirmation.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/order_history.html', {'orders': orders})
