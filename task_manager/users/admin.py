from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UsersAdmin(UserAdmin):
    model = User
    list_display = ["username"]


admin.site.register(User, UsersAdmin)
