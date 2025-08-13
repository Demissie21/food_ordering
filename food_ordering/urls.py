from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import path
from django.views.generic import RedirectView
urlpatterns = [
    path('login/', RedirectView.as_view(url='/accounts/login/'), name='login_redirect'),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/menu/')),  # Redirect root URL to /menu/
    path('', include('main.urls')),  # Include your app URLs here
    path('accounts/', include('django.contrib.auth.urls')),
]
