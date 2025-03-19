from django.urls import path
from . import views

urlpatterns = [
    # User Authentication URLs
    path('', views.home, name='home'),  # Home Page
    path('register/', views.register, name='register'),  # User Registration
    path('login/', views.user_login, name='login'),  # User Login
    path('logout/', views.user_logout, name='logout'),  # User Logout
    path('profile/', views.profile, name='profile'),  # User Profile

    # CRUD URLs for Blog Posts
    path('posts/', views.PostListView.as_view(), name='post-list'),  # View all posts
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # Search URL
    path('search/', views.search, name='search'),  # Search results page

    # Tag filtering URL
    path('tags/<str:tag_name>/', views.tag_posts, name='tag-posts'),  # Posts filtered by tag
]
