from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.menu, name='menu'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('place-order/', views.place_order, name='place_order'),
]
