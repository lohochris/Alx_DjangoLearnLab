from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from django.http import JsonResponse
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

def api_root(request):
    return JsonResponse({"message": "Welcome to the API", "endpoints": ["books/", "booklist/"]})

app_name = 'api'

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('booklist/', BookList.as_view(), name='book-list'),  # Explicitly adding BookList
]
