from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.notifications.models import qpNotification

class qpNotificationSeenSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpNotification
        fields = ["id", "is_seen"]
        read_only_fields = ["id"]
