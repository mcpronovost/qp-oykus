from django.contrib import admin
from qp.projects.models import qpProject

@admin.register(qpProject)
class qpProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "creator", "is_public", "is_active"]
    list_filter = ["is_public", "is_active"]
    readonly_fields = ["created_at", "updated_at"]
