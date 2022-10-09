from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from qp.users.models import qpUserProfile

User = get_user_model()

class qpUserProfileInline(admin.StackedInline):
    model = qpUserProfile

class qpUserAdmin(UserAdmin):
    list_display = ["username", "is_active"]
    list_filter = ["is_active"]
    readonly_fields = ["date_joined", "last_login"]
    fieldsets = (
        ("Personal Information", {
            "fields": [
                "username",
                "email",
                "password",
                "date_joined",
                "last_login"
            ]
        }),
        ("Permissions", {
            "fields": [
                "is_active",
                "is_staff",
                "is_superuser"
            ]
        })
    )
    inlines = [qpUserProfileInline]

admin.site.unregister(User)
admin.site.register(User, qpUserAdmin)
admin.site.unregister(Group)
