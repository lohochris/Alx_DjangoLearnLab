from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.apps import apps  # Import this for get_model()
from django.utils.html import format_html  # Optional: For better display customization

class PublishedYearFilter(admin.SimpleListFilter):
    title = _('publication year')
    parameter_name = 'publication_year'

    def lookups(self, request, model_admin):
        # Use get_model() inside a method to avoid AppRegistryNotReady error
        Book = apps.get_model('bookshelf', 'Book')
        years = set(book.published_date.year for book in Book.objects.all())
        return [(year, year) for year in sorted(years, reverse=True)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(published_date__year=self.value())
        return queryset

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_year')  # Added ISBN
    list_filter = (PublishedYearFilter,)  # Custom filter
    search_fields = ('title', 'author', 'isbn')

    @admin.display(ordering='published_date', description='Publication Year')
    def publication_year(self, obj):
        return obj.published_date.year


# Register the model using a safe method
Book = apps.get_model('bookshelf', 'Book')
admin.site.register(Book, BookAdmin)
