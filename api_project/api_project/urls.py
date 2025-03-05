from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from api.views import BookList  # Import BookList view

# Function-based view to handle the root URL "/"
def home(request):
    return JsonResponse({
        "message": "Welcome to the Django API",
        "endpoints": ["/admin/", "/api/books/", "/api/books-list/"]
    })

urlpatterns = [
    path('', home, name='home'),  # Handle requests to "/"
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API routes
    path('api/books-list/', BookList.as_view(), name='book-list'),  # Ensure BookList is added
]
