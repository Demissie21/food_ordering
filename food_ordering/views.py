from django.shortcuts import render


def order_success(request):
    return render(request, 'main/order_success.html')
