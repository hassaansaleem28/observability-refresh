from django.contrib import admin
from django.urls import path
from api.views import (
    fast_ping,
    force_error,
    slow_request,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ping/', fast_ping),
    path('api/slow/', slow_request),
    path('api/error/', force_error),
]