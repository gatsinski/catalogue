from django.contrib import admin

from .models import Author, Book
from catalogue.contrib.stores.models import Store


@admin.register(Author)
class AuthorsAdmin(admin.ModelAdmin):
    list_filter = ("name", "created_at", "updated_at")
    list_display = ("name", "created_at", "updated_at")
    list_per_page = 15
    date_hierarchy = "created_at"
    search_fields = ("name", "authors", "notes")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user

        return form


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_filter = ("authors", "tags", "created_at", "updated_at")
    list_display = ("title", "created_at", "updated_at")
    list_per_page = 15
    date_hierarchy = "created_at"
    search_fields = ("title", "authors", "notes")
