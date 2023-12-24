"""
Django admin customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Organization, User, PasswordReset, OTP


class UserAdmin(BaseUserAdmin):
    """Defines the admin pages for users."""

    ordering = ["-id"]
    list_display = [
        "id",
        "uid",
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "organization",
        "kind",
        "status",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "organization",
                    "phone_number",
                    "password",
                    "first_name",
                    "last_name",
                    "image",
                    "kind",
                    "status",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "organization",
                    "phone_number",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "image",
                    "kind",
                    "status",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "uid", "name", "country")


admin.site.register(Organization, OrganizationAdmin)
