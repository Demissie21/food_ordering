from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Your app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Login/logout URLs
]
