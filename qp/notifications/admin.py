from django.contrib import admin
from qp.notifications.models import qpNotification

@admin.register(qpNotification)
class qpNotificationAdmin(admin.ModelAdmin):
    list_display = ["user_to", "user_from", "has_type", "is_seen"]
    list_filter = ["has_type", "is_seen"]
