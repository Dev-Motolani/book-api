from django.contrib import admin
from .models import Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'bio')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'isbn', 'date_published')
    

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)