from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import BlogUserCreationForm, BlogUserChangeForm
from .models import User


class BlogUserAdmin(UserAdmin):
    add_form = BlogUserCreationForm
    form = BlogUserChangeForm
    model = User
    list_display = ("email", "username",  "is_staff", "is_active",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, BlogUserAdmin)