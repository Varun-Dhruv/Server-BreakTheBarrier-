
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'password','gender'
    )


admin.site.register(CustomUser, CustomUserAdmin)
