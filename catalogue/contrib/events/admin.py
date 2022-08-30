from django.contrib import admin

from .models import Event
from catalogue.contrib.stores.models import Store


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = ("type",  "location", "tags","created_at", "updated_at")
    list_display = ("name", "type", "location", "created_at", "updated_at")
    list_per_page = 15
    date_hierarchy = "created_at"
    search_fields = ("location", "name", "notes")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user

        return form
