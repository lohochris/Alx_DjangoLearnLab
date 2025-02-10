from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in the list view
    search_fields = ('title', 'author')  # Enable search functionality
    list_filter = ('publication_year',)  # Add filters

# Alternatively, if you don't want customization, just use:
# admin.site.register(Book)
