from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router for automatically generating routes
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),  # This automatically registers book endpoints
]
