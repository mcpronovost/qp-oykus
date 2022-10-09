from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers

from qp.users.models import qpUserProfile

User = get_user_model()

class qpMeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, source="user.id")
    username = serializers.CharField(read_only=True, source="user.username")

    class Meta:
        model = qpUserProfile
        fields = ["id", "username", "name", "slug"]
