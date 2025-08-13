from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_history(request):
    """
    Display all orders placed by the logged-in user,
    ordered by most recent first.
    """
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'main/order_history.html', {'orders': orders})

@login_required
def order_success(request):
    """
    Show a confirmation page after successful order placement.
    """
    return render(request, 'main/order_success.html')
