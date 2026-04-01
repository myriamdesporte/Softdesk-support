from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom admin for User model."""

    list_display = (
        "username",
        "email",
        "age",
        "can_be_contacted",
        "can_data_be_shared",
        "is_staff",
    )
    list_filter = ("is_staff", "is_superuser", "can_be_contacted", "can_data_be_shared")

    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "GDPR Information",
            {"fields": ("date_of_birth", "can_be_contacted", "can_data_be_shared")},
        ),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (
            "GDPR Information",
            {"fields": ("date_of_birth", "can_be_contacted", "can_data_be_shared")},
        ),
    )
