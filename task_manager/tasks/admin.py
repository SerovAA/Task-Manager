from django.contrib import admin

from .models import Tasks


@admin.register(Tasks)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "status",
        "executor",
        "time_create",
    )
    list_display_links = (
        "id",
        "name",
    )
