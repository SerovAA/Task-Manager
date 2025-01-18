from django.contrib import admin

from .models import Statuses


@admin.register(Statuses)
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