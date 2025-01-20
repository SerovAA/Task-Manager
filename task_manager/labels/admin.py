from django.contrib import admin

from .models import Labels


@admin.register(Labels)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "time_create",
    )
    list_display_links = (
        "id",
        "name",
    )