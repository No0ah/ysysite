from django.contrib import admin
from django.urls import path, include
from core.views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api_root'),
]
