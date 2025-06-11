from django.contrib import admin
from .models import Publisher, Author, Profile, Book


# Publisher Admin
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'country', 'website']
    list_filter = ['country', 'city']
    search_fields = ['name', 'city', 'country']
    ordering = ['name']

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'website')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state_province', 'country')
        }),
    )


# Author Admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'birth_date', 'get_books_count']
    list_filter = ['birth_date']
    search_fields = ['name', 'email']
    date_hierarchy = 'birth_date'
    ordering = ['name']

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'birth_date')
        }),
        ('Biography', {
            'fields': ('bio',),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )

    def get_books_count(self, obj):
        return obj.books.count()

    get_books_count.short_description = 'Books Written'


# Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'author', 'website']
    list_filter = ['author']
    search_fields = ['user', 'website']
    raw_id_fields = ['author']  # Makes author selection easier with many authors

    fieldsets = (
        ('User Information', {
            'fields': ('user', 'author')
        }),
        ('Additional Info', {
            'fields': ('bio', 'website')
        }),
    )


# Book Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_authors', 'publisher', 'publication_date']
    list_filter = ['publication_date', 'publisher', 'authors']
    search_fields = ['title', 'authors__name', 'publisher__name']
    date_hierarchy = 'publication_date'
    filter_horizontal = ['authors']  # Nice widget for many-to-many fields
    raw_id_fields = ['publisher']
    ordering = ['-publication_date']

    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'authors', 'publication_date')
        }),
        ('Publishing', {
            'fields': ('publisher',)
        }),
    )

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    get_authors.short_description = 'Authors'

# Alternative: Simple registration (if you prefer less customization)
# admin.site.register(Publisher)
# admin.site.register(Author)
# admin.site.register(Profile)
# admin.site.register(Book)


