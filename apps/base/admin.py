from dataclasses import fields
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ("title",)
        }),
        ("Users", {
            "classes": ("collapse",),
            "fields": ("users",),
            # "read_only": ("users",),
        })
    ]


class CustomerUserAdmin(UserAdmin):
    fieldsets = [
        (None, {
            "fields": ("username", "password"),
        }),
        ("Personal Info", {
            "fields": ("first_name", "last_name", "phone", "email"),
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
        ("Important Dates", {
            "fields": ("last_login", "date_joined")
        })
    ]
    list_display = ["username", "phone", "email", "is_active", "is_superuser"]


admin.site.register(Course, CourseAdmin)
admin.site.register(User, CustomerUserAdmin)
