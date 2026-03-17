from django.contrib import admin
from django.urls import path
from api.views import (
    fast_ping,
    force_error,
    hello_world,
    random_outcome,
    slow_request,
    user_profile,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_world),
    path('api/ping/', fast_ping),
    path('api/slow/', slow_request),
    path('api/random/', random_outcome),
    path('api/error/', force_error),
    path('api/users/<int:user_id>/', user_profile),
]