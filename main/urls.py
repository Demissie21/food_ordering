from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order_history/', views.order_history, name='order_history'),
    path('register/', views.register, name='register'),
]
