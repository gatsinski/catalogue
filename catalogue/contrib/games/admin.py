from django.contrib import admin

from .models import Game
from catalogue.contrib.stores.models import Store


@admin.register(Game)
class GamesAdmin(admin.ModelAdmin):
    list_filter = ("owner", "store", "tags", "created_at", "updated_at")
    list_display = ("title", "owner", "store", "created_at", "updated_at")
    list_per_page = 15
    date_hierarchy = "created_at"
    search_fields = ("title", "notes")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['owner'].initial = request.user
        form.base_fields['store'].initial = request.user.default_store

        return form
