from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from django.http import JsonResponse
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# Optional API root view for `/api/` to return a JSON response instead of a 404 error
def api_root(request):
    return JsonResponse({"message": "Welcome to the API", "endpoints": ["books/", "books-list/"]})

app_name = 'api'  # Namespace for URL resolution

urlpatterns = [
    path('', api_root, name='api-root'),  # Serve a root response at /api/
    path('', include(router.urls)),  # Include router-generated URLs (e.g., /api/books/)
    path('books-list/', BookList.as_view(), name='book-list'),  # ✅ Include BookList view
    path('token/', obtain_auth_token, name='api_token_auth'),
]
