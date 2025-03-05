"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Function-based view to handle the root URL "/"
def home(request):
    return JsonResponse({
        "message": "Welcome to the Django API",
        "endpoints": ["/admin/", "/api/books/"]
    })

urlpatterns = [
    path('', home, name='home'),  # Handle requests to "/"
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API routes
]
