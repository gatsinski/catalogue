from django.contrib import admin

from .models import Game


@admin.register(Game)
class GamesAdmin(admin.ModelAdmin):
    list_filter = ("title", "owner", "store", "tags", "created_at", "updated_at")
    list_display = ("title", "owner", "store", "created_at", "updated_at")
    list_per_page = 15
    date_hierarchy = "created_at"
    search_fields = ("title", "notes")
