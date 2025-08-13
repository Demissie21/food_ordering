from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('menu/', views.menu, name='menu'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_success/', views.order_success, name='order_success'),  # This line requires order_success view
]
